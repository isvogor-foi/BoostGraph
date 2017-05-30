from graph_tool.all import *
import numpy as np


def sample_k(max):
    accept = False
    while not accept:
        k = np.random.randint(1,max+1)
        accept = np.random.random() < 1.0/k
    return k
g = random_graph(20, lambda: sample_k(40), model="probabilistic-configuration",
                 edge_probs=lambda i, k: 1.0 / (1 + abs(i - k)), directed=False,
                 n_iter=10)

pos = random_layout(g)

graph_draw(g, pos, vertex_text=g.vertex_index, vertex_font_size=13, output_size=(500, 500))