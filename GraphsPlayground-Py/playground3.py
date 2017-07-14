import sys
from graph_tool.all import *
import numpy as np
import time
import itertools
import random
from datetime import datetime


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
    def __init__(self, nodes):
        self.__points = np.random.random((nodes, 2)) * 4
        #self.__g, self.__pos_tmp = triangulation(self.__points, type="delaunay")

        #points = np.random.random((self.__nodes, 2)) * 4
        #g, pos = triangulation(points, type="delaunay")
        # g.save("graph-output.xml")
        #g = load_graph("temp.xml")
        self.__g = load_graph("/home/ivan/Downloads/temp-graph.xml")
        self.__pos = fruchterman_reingold_layout(self.__g)
        self.__weight = self.__g.new_edge_property("double")
        #g.save("temp.xml")

    def closeness_graph(self, output=None):
        b = closeness(self.__g)
        print("Res: ", b.ma)
        b = closeness(self.__g)
        graph_draw(self.__g, pos=self.__pos, output_size=(800, 600), vertex_text=self.__g.vertex_index, vertex_fill_color=b, output=output)

    def betweenness_graph(self):
        bv, be = betweenness(self.__g)
        be.a /= be.a.max() / 10
        graph_draw(self.__g, pos=self.__pos, vertex_fill_color=bv, edge_pen_width=be)

    def min_spanning_tree(self):
        for e in self.__g.edges():
            self.__weight[e] = np.linalg.norm(self.__pos[e.target()].a - self.__pos[e.source()].a)
        tree = min_spanning_tree(self.__g, weights=self.__weight)
        u = GraphView(self.__g, efilt=tree)
        graph_draw(u, pos=self.__pos)

    def all_paths(self, output=None):
        c = closeness(self.__g)
        #print("Sorted: ", sorted(c.ma, reverse=True))
        #print("Sorted: ", self.g)
        # --- Construct tree
        # TODO: (max) independent vertex set -> it seems it doesn't produce a unique solution (NP hard)
        # TODO: shortest distance_
        #

        max_closeness = 11
        temp = self.__g.copy()
        edges_list_unique = []
        # remove all edges
        for edge in self.__g.edges():
            temp.remove_edge(edge)

        # get a tree with duplicate edges
        for node in self.__g.vertices():
            vlist, elist = shortest_path(self.__g, max_closeness, node)
            temp.add_edge_list(elist)

        # remove duplicates
        tree = temp.copy()
        for e in temp.edges():
            if str(e) not in edges_list_unique:
                edges_list_unique.append(str(e))
            else:
                tree.remove_edge(e)

        graph_draw(tree, pos=self.__pos, vertex_text=tree.vertex_index, vertex_fill_color=c, output=output)

    def non_neigbour_vertices(self):
        c = closeness(self.__g)
        c_list = []
        #print("Sorted: ", sorted(c.ma, reverse=True))
        for i, cls in enumerate(c):
            c_list.append([i, cls])
        #print("Sorforted: ", sorted(c_list, key=lambda x: x[1]))
        c_list = sorted(c_list, key=lambda x: x[1])

        no_duplicate_tree = self.remove_duplicates(self.__g.copy())

        # find n non neigbours in the list of central nodes starting from the least central
        roots = []
        roots.append(c_list[0][0])

        for node, cls in c_list:
            pushit = True
            for root in roots:
                if self.are_neighbors(no_duplicate_tree, root, node) or node is root:
                    pushit = False
            if pushit:
                roots.append(node)

        return roots

    def new_thing(self):
        self.__g = self.remove_duplicates(self.__g.copy())
        c = closeness(self.__g)

        root_candidates = self.non_neigbour_vertices()
        root_candidates = self.sorted_by_degree(root_candidates)

        print("Root candidates: ", root_candidates)

        edgeless_graph_copy = self.__g.copy()
        for edge in self.__g.edges():
            edgeless_graph_copy.remove_edge(edge)

        depth = 8

        #TODO: HERE!!!
        v_pos = fruchterman_reingold_layout(self.__g)
        #graph_draw(self.__g, output_size=(1024, 800), pos=v_pos, vertex_text=self.__g.vertex_index)
        forest = self.construct_tree_balanced(self.__g.copy(), root_candidates[:5], depth)

        #forest = self.construct_tree_balanced(self.g.copy(), [14,15,5], depth)
        #forest = self.construct_tree_balanced(self.g.copy(), [14,18,17], depth)

        print("Done with forest generation, drawing...")
        #self.draw_mynode_tree(depth, forest, edgeless_graph_copy)
        for tree in forest:
            subgraph, v_prop = self.get_tree(tree, depth)
            #self.remove_duplicates(subgraph)
            #graph_draw(subgraph, pos=fruchterman_reingold_layout(subgraph), vertex_text=v_prop)

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

        #graph_draw(graph_copy, output_size=(1024, 800), pos=self.__pos, vertex_text=graph_copy.vertex_index)
        #res = max_independent_vertex_set(graph_copy)
        #graph_draw(graph_copy, output_size=(1024, 800), pos=self.__pos, vertex_fill_color=res, vertex_text=graph_copy.vertex_index)

        return graph_copy

    # -------------------------------------------------------------------------------

    def sorted_by_degree(self, existing_candidates):
        d_list = [] # existing_candidates

        for t_vertex in self.__g.vertices():
            d_list.append([int(t_vertex), t_vertex.out_degree()])

        d_list = [item[0] for item in sorted(d_list, key=lambda x: x[1])]

        for candidate in d_list:
            if candidate not in existing_candidates:
                existing_candidates.append(candidate)

        return existing_candidates

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

        subgraph = self.__g.copy()
        v_prop = subgraph.new_vertex_property("string")

        # create a subgraph by removing nodes not in the tree
        for vertex in reversed(sorted(self.__g.get_vertices())):
            if int(vertex) not in subtree_vertices:
                subgraph.remove_vertex(int(vertex))
            else:
                v_prop[subgraph.vertex(vertex)] = str(vertex)

        #print("ALL: ", subtree_vertices, " v_prop: ", v_prop)
        print("ALL: ", subtree_vertices)

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
        graph_draw(original_graph, pos=self.__pos, vertex_text=original_graph.vertex_index)

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
        graph_draw(dual_tree, pos=self.__pos, vertex_text=dual_tree.vertex_index)

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
    for i in range(1, 10):
        start_time = time.time()
        graphs = Graphs(i * 10)
        #graphs.min_spanning_tree()
        #graphs.closeness_graph()
        #graphs.betweenness_graph()
        graphs.new_thing()
        elapsed_time = time.time() - start_time
        print("Run: ", i, ", runtime: ", elapsed_time)
        #graphs.all_paths()



