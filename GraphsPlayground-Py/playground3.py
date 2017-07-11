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
    #points = np.random.random((30, 2)) * 4
    #g, pos = triangulation(points, type="delaunay")
    # g.save("graph-output.xml")
    g = load_graph("temp.xml")
    #g = load_graph("/home/ivan/Downloads/temp-graph.xml")
    pos = fruchterman_reingold_layout(g)
    weight = g.new_edge_property("double")
    #g.save("temp.xml")

    def closeness_graph(self, output=None):
        b = closeness(self.g)
        print("Res: ", b.ma)
        b = closeness(self.g)
        graph_draw(self.g, pos=self.pos, output_size=(800, 600), vertex_text=self.g.vertex_index, vertex_fill_color=b, output=output)

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

        #for my_list in sorted(my_nodes, reverse=True):
        #    print("Node: ", my_list.get_node())

        # dual_tree = self.g.copy()
        # temp_tree = self.g.copy()
        # for edge in self.g.edges():
        #     dual_tree.remove_edge(edge)
        #
        # self.construct_tree_from_old(dual_tree, temp_tree, 5, 3)

        edgeless_graph_copy = self.g.copy()
        for edge in self.g.edges():
            edgeless_graph_copy.remove_edge(edge)

        depth = 5
        no_duplicate_tree = self.remove_duplicates(self.g.copy())
        forest = self.construct_tree_balanced(no_duplicate_tree, [18, 15], depth)
        print("Done with forest generation, drawing...")
        self.draw_mynode_tree(depth, forest, edgeless_graph_copy)

        ## temp
        #g2 = self.g.copy()
        #self.remove_duplicates(g2)
        # end temp

        for tree in forest:
            subgraph, v_prop = self.get_tree(tree, depth)
            #self.remove_duplicates(subgraph)
            graph_draw(subgraph, pos=fruchterman_reingold_layout(subgraph), vertex_text=v_prop)

    def remove_duplicates(self, original_graph):
        graph_copy = original_graph.copy()
        graph_copy.clear_edges()
        taken_list = []

        for graph_edge in original_graph.edges():
            source = int(graph_edge.source())
            target = int(graph_edge.target())
            current = [target, source]
            current_reversed = [source, target]
            if current not in taken_list and target in original_graph.vertices():
                graph_copy.add_edge(graph_edge.source(), graph_edge.target())
                taken_list.append(current)
                taken_list.append(current_reversed)

        #graph_draw(graph_copy, pos=self.pos, vertex_text=graph_copy.vertex_index)
        return graph_copy

    # -------------------------------------------------------------------------------

    def get_tree(self, branch, max_depth):
        current_children_list = branch.get_children()
        subtree_vertices = list()
        subtree_vertices.append(branch.get_id())
        current_depth = 0

        while current_depth < max_depth:
            # draw verices
            next_children_list = []
            for current_child in current_children_list:
                subtree_vertices.append(current_child.get_id())
                for child in current_child.get_children():
                    next_children_list.append(child)
            # go to next level depth
            current_depth += 1
            current_children_list = next_children_list
        # while current_depth < max_depth:
        #     # draw verices
        #     for current_child in current_children_list:
        #         all.append(current_child.get_id())
        #
        #     # go to next level depth
        #     current_depth += 1
        #     next_children_list = []
        #     for current_child in current_children_list:
        #         for child in current_child.get_children():
        #             next_children_list.append(child)
        #     current_children_list = next_children_list

        subgraph = self.g.copy()
        v_prop = subgraph.new_vertex_property("string")

        # create a subgraph by removing nodes not in the tree
        for vertex in reversed(sorted(self.g.get_vertices())):
            if int(vertex) not in subtree_vertices:
                subgraph.remove_vertex(int(vertex))
            else:
                v_prop[subgraph.vertex(vertex)] = str(vertex)

        print("ALL: ", subtree_vertices, " v_prop: ", v_prop)
        return subgraph, v_prop

    def construct_tree_balanced(self, original_graph, roots, depth):
        # --- Experimental
        # 1, 5, 11, 14, 18
        graph_nodes = []
        taken_nodes = []

        for root in roots:
            graph_nodes.append(TreeNode(root, 0))
            taken_nodes.append(root)
        d = 0

        current_depth_nodes = graph_nodes
        increase_depth = False

        while d < depth:
            # if going to next depth level, set the nodes
            if increase_depth:
                #print("Next level: ", d)
                next_depth_nodes = []
                for p in current_depth_nodes:
                    # zip the lists otherwise you are greedy again
                    next_depth_nodes = list(itertools.chain.from_iterable(
                        itertools.zip_longest(next_depth_nodes, p.get_children())))
                current_depth_nodes = list(filter(None.__ne__, next_depth_nodes))
                increase_depth = False
            if not current_depth_nodes:
                break

            # add new children, non-greedy
            empty_set_counter = len(current_depth_nodes)
            for i in current_depth_nodes:
                temp = self.get_free_neighbor_new(i, original_graph, taken_nodes)
                if temp is not -1:
                    taken_nodes.append(temp)
                    new_node = TreeNode(temp, d + 1);
                    new_node.set_parent(i)
                    i.set_child(new_node)
                    #print(i, " takes: ", temp)
                else:
                    empty_set_counter -= 1
                    # I fetched empty for each branch, go to next level
                    if empty_set_counter is 0:
                        d += 1
                        increase_depth = True
        return graph_nodes

    def draw_mynode_tree(self, depth, graph_nodes, original_graph):
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
        graph1_final.append([18, 15])
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
    graphs.closeness_graph()
    #graphs.betweenness_graph()
    graphs.new_thing()
    graphs.all_paths()



