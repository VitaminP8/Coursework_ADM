import networkx as nx
import matplotlib.pyplot as plt
from graph.graf_algs import bfs, dfs, greedy_coloring

# Создание пустого графа
G = nx.Graph()

# Добавление вершин в граф
num_vertices = 19
vertices = range(num_vertices)
G.add_nodes_from(vertices)

# Добавление ребер в граф (пример случайного соединения)
edges = [
    (0, 1), (0, 2), (0, 3), (1, 4), (1, 5),
    (2, 6), (2, 7), (3, 8), (3, 9), (4, 10),
    (4, 11), (4, 12), (8, 13), (9, 14), (9, 15),
    (10, 16), (10, 17), (14, 18)
]
G.add_edges_from(edges)

# Визуализация графа
nx.draw(G, with_labels=True)
plt.show()

bfs(G, 0)
dfs(G, 0)

coloring, num_colors = greedy_coloring(G)
print("Раскраска вершин графа:")
for node, color in coloring.items():
    print(f"Вершина {node}: Цвет {color}")

print("Количество используемых цветов:", num_colors)