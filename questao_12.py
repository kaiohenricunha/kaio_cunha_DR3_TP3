import time
import random
import math
import heapq

def generate_random_graph_list(num_vertices, edge_prob=0.3, max_weight=10):
    """
    Gera um grafo no formato de lista de adjacência.
    Cada vértice é inteiro de 0 a num_vertices-1.
    """
    graph = {i: [] for i in range(num_vertices)}
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and random.random() < edge_prob:
                weight = random.randint(1, max_weight)
                graph[i].append((j, weight))
    return graph

def generate_random_graph_matrix(num_vertices, edge_prob=0.3, max_weight=10):
    """
    Gera um grafo no formato de matriz (dicionário de dicionários).
    Usa infinito para indicar ausência de conexão e zero na diagonal.
    """
    vertices = list(range(num_vertices))
    graph = {i: {j: math.inf for j in vertices} for i in vertices}
    for i in vertices:
        graph[i][i] = 0
        for j in vertices:
            if i != j and random.random() < edge_prob:
                graph[i][j] = random.randint(1, max_weight)
    return vertices, graph

def dijkstra(graph, start):
    """
    Executa o algoritmo de Dijkstra para encontrar os menores caminhos a partir de 'start'.
    Retorna um dicionário com a distância mínima para cada vértice.
    """
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        dist, vertex = heapq.heappop(queue)
        if dist > distances[vertex]:
            continue
        for neighbor, weight in graph[vertex]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
    return distances

def floyd_warshall(vertices, graph):
    """
    Executa o algoritmo de Floyd-Warshall para encontrar os menores caminhos entre todos os pares.
    Retorna um dicionário de dicionários com as distâncias mínimas.
    """
    # Inicializa a matriz de distâncias
    dist = {i: {j: graph[i][j] for j in vertices} for i in vertices}
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def measure_algorithms(num_vertices, edge_prob=0.3, max_weight=10):
    """
    Gera um grafo aleatório nos dois formatos e mede o tempo de execução:
      - Dijkstra: executado para cada vértice como origem.
      - Floyd-Warshall: executado uma única vez.
    Retorna os tempos de execução de cada algoritmo.
    """
    # Gera o grafo para Dijkstra (lista de adjacência)
    graph_list = generate_random_graph_list(num_vertices, edge_prob, max_weight)
    # Gera o grafo para Floyd-Warshall (matriz)
    vertices, graph_matrix = generate_random_graph_matrix(num_vertices, edge_prob, max_weight)
    
    # Mede Dijkstra (todos os vértices como origem)
    start_time = time.perf_counter()
    for v in range(num_vertices):
        dijkstra(graph_list, v)
    dijkstra_time = time.perf_counter() - start_time

    # Mede Floyd-Warshall
    start_time = time.perf_counter()
    floyd_warshall(vertices, graph_matrix)
    fw_time = time.perf_counter() - start_time

    return dijkstra_time, fw_time

def main():
    sizes = [10, 20, 50, 100]
    for n in sizes:
        dt, ft = measure_algorithms(n)
        print(f"Vértices: {n}, Dijkstra total: {dt:.6f}s, Floyd-Warshall: {ft:.6f}s")

if __name__ == '__main__':
    main()
