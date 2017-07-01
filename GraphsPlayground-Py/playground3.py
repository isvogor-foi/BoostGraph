import sys
from graph_tool.all import *
import numpy as np
import time
from itertools import chain

# https://graph-tool.skewed.de/static/doc/generation.html
class MyNodes:
    def __init__(self, node, centrality):
        self.__graph_node = node
        self.__centrality = centrality

    def __lt__(self, other):
        return self.__centrality < other.__centrality

    def get_centrality(self):
        return self.__centrality

    def get_node(self):
        return self.__graph_node

class MyNewNode:
    def __init__(self, id):
        self.__id = id
        self.__children = []

    def get_id(self):
        return self.__id

    def add_child(self, child):
        self.__children.append(child)

    def get_children(self):
        return self.__children

    def __str__(self):
        return str(self.__id) + " children: " + str(len(self.__children))


class Graphs:
    #points = np.random.random((30, 2)) * 4
    #g, pos = triangulation(points, type="delaunay")
    # g.save("graph-output.xml")
    g = load_graph("temp.xml")
    pos = fruchterman_reingold_layout(g)
    weight = g.new_edge_property("double")
    #g.save("temp.xml")

    def closeness_graph(self, output=None):
        b = closeness(self.g)
        print("Res: ", b.ma)
        b = closeness(self.g)
        graph_draw(self.g, pos=self.pos, output_size=(600, 600), vertex_text=self.g.vertex_index, vertex_fill_color=b, output=output)

    def betweenness_graph(self):
        bv, be = betweenness(self.g)
        be.a /= be.a.max() / 10
        graph_draw(self.g, pos=self.pos, vertex_fill_color=bv, edge_pen_width=be)

    def min_spanning_tree(self):
        for e in self.g.edges():
            self.weight[e] = np.linalg.norm(self.pos[e.target()].a - self.pos[e.source()].a)
        tree = min_spanning_tree(self.g, weights=self.weight)
        u = GraphView(self.g, efilt=tree)
        graph_draw(u, pos=self.pos)

    def all_paths(self, output=None):
        c = closeness(self.g)
        print("Sorted: ", sorted(c.ma, reverse=True))
        print("Sorted: ", self.g)
        # --- Construct tree

        max_closeness = 11
        temp = self.g.copy()
        edges_list_unique = []
        # remove all edges
        for edge in self.g.edges():
            temp.remove_edge(edge)

        # get a tree with duplicate edges
        for node in self.g.vertices():
            vlist, elist = shortest_path(self.g, max_closeness, node)
            temp.add_edge_list(elist)

        # remove duplicates
        tree = temp.copy()
        for e in temp.edges():
            if str(e) not in edges_list_unique:
                edges_list_unique.append(str(e))
            else:
                tree.remove_edge(e)

        graph_draw(tree, pos=self.pos, vertex_text=tree.vertex_index, vertex_fill_color=c, output=output)

    def new_thing(self):
        c = closeness(self.g)
        my_var = c.ma
        print("My var", type(my_var))
        my_nodes = []

        counter = 0
        for node in np.nditer(my_var):
            my_nodes.append(MyNodes(counter, node))
            counter = counter + 1

        print("Vertex: ", type(self.g.vertices()))
        print("Vertex: ", np.isin(1, self.g.get_vertices()))

        print("Neighbors: ", self.are_neighbors(self.g, 11, 13))
        print("Distance: ", self.distance_to(self.g, 10, 13))

        #for my_list in sorted(my_nodes, reverse=True):
        #    print("Node: ", my_list.get_node())

        dual_tree = self.g.copy()
        temp_tree = self.g.copy()
        for edge in self.g.edges():
            dual_tree.remove_edge(edge)

        # --- Experimental
        # 1, 5, 11, 14, 18
        graph1 = []
        graph1_final = []
        graph1_free_nodes = range(0, 30)
        graph2 = []

        graph1_final.append([5])
        for i in range(0, 6):
            graph1 = graph1_final[i]
            for k in graph1:
                temp = self.get_neighbors(temp_tree, k)
                fin = list(chain.from_iterable(graph1_final))
                f = []
                for i in temp:
                    if i not in fin:
                        f.append(i)
                graph1_final.append(f)

        print("Temp: ", len(graph1_final))
        print("Graph: ", graph1_final)

        child_index = 1
        for k in range(0, 6):
            lenf = len(graph1_final[k])
            for i in range(0, lenf):
                children = graph1_final[child_index]
                for j in children:
                    dual_tree.add_edge(graph1_final[k][i], j)
                child_index += 1

        graph_draw(dual_tree, pos=self.pos, vertex_text=dual_tree.vertex_index)

    def get_neighbors(self, graph, source):
        neighbors = []
        #neighbors.append(source)
        for node in graph.vertices():
            if self.distance_to(graph, source, node) is 1:
                neighbors.append(int(node))
        return neighbors

    def are_neighbors(self, graph, start_node, end_node):
        for edge in graph.edges():
            if int(edge.source()) is start_node and int(edge.target()) is end_node:
                return True
            if int(edge.target()) is start_node and int(edge.source()) is end_node:
                return True
        return False

    def distance_to(self, graph, start_node, end_node):
        for node in graph.vertices():
            if int(node) is start_node:
                vlist, elist = shortest_path(graph, end_node, node)
                #print("Edges: ", elist)
                return len(elist)


if __name__ == '__main__':
    graphs = Graphs()
    #graphs.min_spanning_tree()
    #graphs.closeness_graph()
    #graphs.betweenness_graph()
    graphs.new_thing()
    graphs.all_paths()



