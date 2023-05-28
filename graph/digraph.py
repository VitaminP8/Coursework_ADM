import networkx as nx
import matplotlib.pyplot as plt
from graph.digraph_algs import dekstra, bellman_ford, prim_mst, kruskal_mst

# Создание пустого ориентированного графа
G = nx.DiGraph()

# Добавление вершин в граф
num_vertices = 8
vertices = range(num_vertices)
G.add_nodes_from(vertices)

# Добавление направленных ребер с весами в граф
edges = [
    (0, 1, {'weight': 2}), (0, 2, {'weight': 3}),
    (1, 3, {'weight': 1}), (1, 4, {'weight': 4}),
    (2, 4, {'weight': 2}), (2, 5, {'weight': 5}),
    (3, 6, {'weight': 2}), (4, 6, {'weight': 3}),
    (4, 7, {'weight': 1}), (5, 7, {'weight': 4}),
    (6, 4, {'weight': 3}),
]
G.add_edges_from(edges)

# Визуализация графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

print(dekstra(G, 0))
print(bellman_ford(G, 0))


mst = prim_mst(G)
pos = nx.spring_layout(mst)
nx.draw(mst, pos, with_labels=True, arrows=True)
edge_labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels)
plt.show()


mst2 = kruskal_mst(G)
pos = nx.spring_layout(mst2)
nx.draw(mst2, pos, with_labels=True, arrows=True)
edge_labels = nx.get_edge_attributes(mst2, 'weight')
nx.draw_networkx_edge_labels(mst2, pos, edge_labels=edge_labels)
plt.show()