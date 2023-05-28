import networkx as nx
import heapq



def dekstra(graph, source):
    # Инициализация словаря для хранения расстояний от источника до вершин
    distances = {vertex: float('inf') for vertex in graph.nodes}
    distances[source] = 0  # Расстояние от источника до самого себя равно 0

    # Создание очереди с приоритетом для выбора вершин с наименьшим расстоянием
    pq = [(0, source)]  # (расстояние, вершина)
    heapq.heapify(pq)

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Пропускаем вершину, если найдено расстояние, которое уже меньше
        if current_distance > distances[current_vertex]:
            continue

        # Просмотр соседних вершин текущей вершины
        for neighbor in graph.neighbors(current_vertex):
            edge_weight = graph.get_edge_data(current_vertex, neighbor)['weight']
            distance = current_distance + edge_weight

            # Если найдено более короткое расстояние, обновляем его
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def bellman_ford(graph, source):
    # Инициализация расстояний до всех вершин как бесконечность
    distances = {vertex: float('inf') for vertex in graph.nodes}
    distances[source] = 0  # Расстояние от источника до самого себя равно 0

    # Проход по всем ребрам n - 1 раз
    num_vertices = len(graph.nodes)
    for _ in range(num_vertices - 1):
        # Проход по всем ребрам графа
        for u, v, edge_data in graph.edges(data=True):
            weight = edge_data['weight']
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Проверка наличия отрицательных циклов
    for u, v, edge_data in graph.edges(data=True):
        weight = edge_data['weight']
        if distances[u] + weight < distances[v]:
            raise ValueError("Граф содержит отрицательный цикл")

    return distances


# минимальное остовой дерево
def prim_mst(graph):
    # Словарь для хранения выбранных вершин и соответствующих ребер
    selected_vertices = {0: None}
    selected_edges = []

    # Выбираем вершины, пока не выберем все
    while len(selected_vertices) < len(graph.nodes):
        min_weight = float('inf')
        min_edge = None
        min_vertex = None

        # Просматриваем выбранные вершины
        for vertex in selected_vertices:
            # Просматриваем соседние вершины текущей вершины
            for neighbor in graph.neighbors(vertex):
                if neighbor not in selected_vertices:
                    edge_weight = graph.get_edge_data(vertex, neighbor)['weight']
                    # Находим минимальное ребро
                    if edge_weight < min_weight:
                        min_weight = edge_weight
                        min_edge = (vertex, neighbor)
                        min_vertex = neighbor

        # Добавляем выбранную вершину и соответствующее ребро
        selected_vertices[min_vertex] = None
        selected_edges.append(min_edge)

    # Создаем остовное дерево на основе выбранных ребер
    mst = nx.DiGraph()
    mst.add_edges_from(selected_edges)

    return mst



def kruskal_mst(graph):
    mst = nx.Graph()  # Пустой граф для хранения минимального остовного дерева
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])  # Сортировка ребер по весу
    uf = nx.utils.UnionFind()  # Структура данных Union-Find для отслеживания компонент связности

    for u, v, weight in edges:
        if uf[u] != uf[v]:  # Проверка на цикл
            mst.add_edge(u, v, weight=weight['weight'])  # Добавление ребра в минимальное остовное дерево
            uf.union(u, v)  # Объединение компонент связности

    return mst