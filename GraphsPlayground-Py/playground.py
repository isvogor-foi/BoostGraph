from graph_tool.all import *

letters = ['a', 'b', 'c', 'd']

# g = load_graph("graph-b.xml")
# pos = radial_tree_layout(g, 0)

# Betwenness

for l in letters:
    g = load_graph("graph-" + l + ".xml")
    pos = fruchterman_reingold_layout(g)
    vp, ep = betweenness(g)
    print("Centrality:", vp.a, ep.a)
    graph_draw(g, pos, vertex_text=g.vertex_index, vertex_font_size=13, output_size=(500, 500), vertex_fill_color=vp)

# Closeness
'''
for l in letters:
    g = load_graph("graph-" + l + ".xml")
    pos = fruchterman_reingold_layout(g)
    vp = closeness(g)
    print("Centrality:", vp.a)
    graph_draw(g, pos, vertex_text=g.vertex_index, vertex_font_size=13, output_size=(500, 500), vertex_fill_color=vp)
'''
# eigenvector
'''
for l in letters:
    g = load_graph("graph-" + l + ".xml")
    pos = fruchterman_reingold_layout(g)
    eval, evec = eigenvector(g)
    print("Centrality:", evec.a)
    graph_draw(g, pos, vertex_text=g.vertex_index, vertex_font_size=13, output_size=(500, 500), vertex_fill_color=evec)
'''
# pagerank
'''
for l in letters:
    g = load_graph("graph-" + l + ".xml")
    pos = fruchterman_reingold_layout(g)
    pr = pagerank(g)
    print("Centrality:", pr.a)
    graph_draw(g, pos, vertex_text=g.vertex_index, vertex_font_size=13, output_size=(500, 500), vertex_fill_color=pr)
'''
# katz (similar as pagerank)
'''
for l in letters:
    g = load_graph("graph-" + l + ".xml")
    pos = fruchterman_reingold_layout(g)
    kc = katz(g)
    print("Centrality:", kc.a)
    graph_draw(g, pos, vertex_text=g.vertex_index, vertex_font_size=13, output_size=(500, 500), vertex_fill_color=kc)
'''
