import sys
from graph_tool.all import *
import numpy as np
import time
import itertools
import random

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

class TreeNode:
    def __init__(self, id, depth):
        self.__id = id
        self.__depth = depth
        self.__children = []

    def get_id(self):
        return self.__id

    def set_parent(self, parent):
        self.__myparent = parent

    def get_parent(self):
        return self.__myparent

    def set_child(self, child):
        self.__children.append(child)

    def get_children(self):
        return self.__children

    def __str__(self):
        my_name = "N: " + str(self.__id) + " C: " + str(len(self.__children))
        return my_name

class Graphs:
    points = np.random.random((30, 2)) * 4
    g, pos = triangulation(points, type="delaunay")
    # g.save("graph-output.xml")
    #g = load_graph("temp.xml")
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

        # dual_tree = self.g.copy()
        # temp_tree = self.g.copy()
        # for edge in self.g.edges():
        #     dual_tree.remove_edge(edge)
        #
        # self.construct_tree_from_old(dual_tree, temp_tree, 5, 3)

        dual_tree = self.g.copy()
        temp_tree = self.g.copy()
        for edge in self.g.edges():
            dual_tree.remove_edge(edge)

        forest = self.construct_tree_balanced(dual_tree, temp_tree, 5, 5)
        for tree in forest:
            subgraph = self.get_tree(tree, 5)
            graph_draw(subgraph, pos=fruchterman_reingold_layout(subgraph), vertex_text=subgraph.vertex_index)


    # -------------------------------------------------------------------------------

    def get_tree(self, branch, max_depth):
        node_list = list()
        node_list.append(branch)
        child_index = 0

        # create the list of all children, i.e. vertices in the given branch
        for depth in range(max_depth):
            #print("Depth: ", depth, " len: ", len(node_list))
            if depth < len(node_list):
                num_children = len(node_list[depth].get_children())
                #print("Depth: ", depth, " Children: ", num_children)
                for i in range(num_children):
                    children = node_list[depth].get_children()
                    for child in children:
                        if child not in node_list:
                            node_list.append(child)
                    child_index += 1

        # get only IDs
        tree_ints = [i.get_id() for i in node_list]

        subgraph = self.g.copy()
        # create a subgraph by removing nodes not in the tree
        for vertex in reversed(sorted(self.g.get_vertices())):
            if int(vertex) not in tree_ints:
                subgraph.remove_vertex(int(vertex))

        return subgraph

    def construct_tree_balanced(self, original_graph, temp_tree, starting_node, depth):
        # --- Experimental
        # 1, 5, 11, 14, 18
        graph_nodes = []
        taken_nodes = []

        graph_nodes.append(TreeNode(29, 0))
        graph_nodes.append(TreeNode(18, 0))
        graph_nodes.append(TreeNode(15, 0))

        taken_nodes.append(29)
        taken_nodes.append(18)
        taken_nodes.append(15)
        d = 0

        current_level_set = graph_nodes
        next_set = []
        go_next_level = False

        while d < depth:
            if go_next_level:
                #print("Next level: ", d)
                next_set = []
                for p in current_level_set:
                    #for c in p.get_children():
                        #next_set.append(c)
                    next_set = list(itertools.chain.from_iterable(itertools.zip_longest(next_set, p.get_children())))
                current_level_set = list(filter(None.__ne__, next_set))
                #print("Set: ", current_level_set)
                go_next_level = False
            if not current_level_set:
                break

            empty_set_counter = len(current_level_set)
            for i in current_level_set:
                temp = self.get_free_neighbor_new(i, temp_tree, taken_nodes)
                if temp is not -1:
                    taken_nodes.append(temp)
                    new_node = TreeNode(temp, d + 1);
                    new_node.set_parent(i)
                    i.set_child(new_node)
                    #print(i, " takes: ", temp)
                else:
                    empty_set_counter -= 1
                    if empty_set_counter is 0:  # I fetched empty for each branch, go to next level
                        d += 1
                        go_next_level = True
        print("Done with forest generation, drawing...")

        current_set = graph_nodes
        d = 0
        while d < depth:
            # draw verices
            for current in current_set:
                for child in current.get_children():
                    original_graph.add_edge(child.get_id(), current.get_id())
            # go to next level depth
            d += 1
            next_set = []
            for p in current_set:
                for c in p.get_children():
                    next_set.append(c)
            current_set = next_set
        # draw solution
        graph_draw(original_graph, pos=self.pos, vertex_text=original_graph.vertex_index)
        return graph_nodes

    # -------------------------------------------------------------------------------

    def get_free_neighbor_new(self, current_node, graph, taken_nodes):
        for node in graph.vertices():
            if self.distance_to(graph, current_node.get_id(), node) is 1 and node not in taken_nodes:
                return int(node)
        return -1

    # -------------------------------------------------------------------------------

    def construct_tree_greedy(self, dual_tree, temp_tree, starting_node, depth):
        # --- Experimental
        # 1, 5, 11, 14, 18
        graph1_final = []
        graph1_final.append([29, 18, 15])
        for j in range(0, depth):
            graph1 = graph1_final[j]
            for k in graph1:
                fin = list(itertools.chain.from_iterable(graph1_final))
                #while self.get_free_neighbor(graph1_final, temp_tree, k, fin) is not []:
                temp = self.get_free_neighbors(graph1_final, temp_tree, k, fin)
                graph1_final.append(temp)
        print("Temp: ", len(graph1_final))
        print("Graph: ", graph1_final)
        child_index = 1

        for k in range(0, depth):
            lenf = len(graph1_final[k])
            for i in range(0, lenf):
                children = graph1_final[child_index]
                for j in children:
                    dual_tree.add_edge(graph1_final[k][i], j)
                child_index += 1
        graph_draw(dual_tree, pos=self.pos, vertex_text=dual_tree.vertex_index)

    def get_neighbors(self, graph, source):
        neighbors = []
        for node in graph.vertices():
            if self.distance_to(graph, source, node) is 1:
                neighbors.append(int(node))
        return neighbors

    def get_free_neighbors(self, graph1_final, graph, source, taken):
        neighbors = []
        for node in graph.vertices():
            if self.distance_to(graph, source, node) is 1:
                # if not taken, take it
                if node not in taken:
                    neighbors.append(int(node))
                #if taken and closer, steal it
                #else:
                #    rooti = self.get_root_of(graph1_final, int(node), 4)
                #    print("Parent of ", int (node), " is ", rooti % 2)

        return neighbors

    def get_free_neighbor(self, graph1_final, graph, source, taken):
        neighbors = []
        for node in graph.vertices():
            if self.distance_to(graph, source, node) is 1:
                if node not in taken:
                    neighbors.append(int(node))
                    return neighbors
        return neighbors

    def get_root_of(self, graph, node, depth):
        child_index = 0
        for k in range(0, depth):
            lenf = len(graph[k])
            for i in range(0, lenf):
                children = graph[child_index]
                for j in children:
                    if graph[k][i] == node:
                        return k
        return 0

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



