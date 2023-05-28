import networkx as nx
from collections import deque


def bfs(graph, start):  # поиск в ширину
    visited = set()  # Множество посещенных вершин
    queue = deque()  # Очередь для обхода

    # Добавляем начальную вершину в очередь и отмечаем ее как посещенную
    queue.append(start)
    visited.add(start)

    while queue:
        vertex = queue.popleft()  # Извлекаем вершину из очереди
        print(vertex)  # Выводим текущую вершину

        # Обходим все смежные вершины
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                queue.append(neighbor)  # Добавляем смежную вершину в очередь
                visited.add(neighbor)  # Отмечаем ее как посещенную




def dfs(graph, start, visited=None):  # поиск в грубину
    if visited is None:
        visited = set()  # Множество посещенных вершин

    visited.add(start)  # Отмечаем текущую вершину как посещенную
    print(start)  # Выводим текущую вершину

    # Обходим все смежные вершины
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Рекурсивно запускаем DFS для смежной вершины


def greedy_coloring(graph):
    coloring = {}  # Словарь для хранения раскраски вершин
    used_colors = set()  # Множество используемых цветов

    # Обход вершин графа
    for node in graph.nodes():
        # Проверка соседних вершин и выбор доступного цвета
        neighbor_colors = {coloring[n] for n in graph.neighbors(node) if n in coloring}
        available_colors = set(range(len(graph))) - neighbor_colors
        if available_colors:
            # Использование минимального доступного цвета
            min_color = min(available_colors)
            coloring[node] = min_color
            used_colors.add(min_color)
        else:
            # Если все цвета уже используются, добавляем новый цвет
            new_color = len(graph)
            coloring[node] = new_color
            used_colors.add(new_color)

    return coloring, len(used_colors)
