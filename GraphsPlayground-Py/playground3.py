from graph_tool.all import *
import numpy as np
import time

# https://graph-tool.skewed.de/static/doc/generation.html

class Graphs:
    # points = np.random.random((30, 2)) * 4
    # g, pos = triangulation(points, type="delaunay")
    # g.save("graph-output.xml")
    g = load_graph("graph-output.xml")
    pos = fruchterman_reingold_layout(g)
    weight = g.new_edge_property("double")

    def closeness_graph(self, output=None):
        b = closeness(self.g)
        print("Res: ", b.ma)
        graph_draw(self.g, pos=self.pos, output_size=(600, 600), vertex_text=self.g.vertex_index, vertex_fill_color=b, output=output)

    def betweenness_graph(self):
        bv, be = betweenness(self.g)
        be.a /= be.a.max() / 10
        graph_draw(self.g, pos=self.pos, vertex_fill_color=bv, edge_pen_width=be)

    def min_spanning_tree(self):
        for e in g.edges():
            weight[e] = np.linalg.norm(pos[e.target()].a - pos[e.source()].a)
        tree = min_spanning_tree(g, weights=weight)
        u = GraphView(g, efilt=tree)
        graph_draw(u, pos=pos)

    def all_paths(self, output=None):
        c = closeness(self.g)
        max_closeness = c.a.argmax()
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


if __name__ == '__main__':
    graphs = Graphs()
    graphs.closeness_graph()
    #graphs.betweenness_graph()
    graphs.all_paths()



