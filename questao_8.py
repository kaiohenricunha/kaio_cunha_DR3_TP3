def floyd_warshall(vertices, grafo):
    """
    vertices: lista dos vértices (bairros).
    grafo: dicionário onde cada chave é um vértice e seu valor é um dicionário com os vizinhos e
           os tempos de deslocamento (pesos). Exemplo:
           {
               'A': {'B': 5, 'C': 10},
               'B': {'C': 3, 'D': 2},
               'C': {'D': 1},
               'D': {}
           }
           
    Retorna uma matriz (dicionário de dicionários) com os menores tempos de deslocamento entre todos os pares.
    """
    # Inicialização da matriz de distâncias.
    dist = {i: {j: float('inf') for j in vertices} for i in vertices}
    for v in vertices:
        dist[v][v] = 0
    for u in grafo:
        for v, peso in grafo[u].items():
            dist[u][v] = peso

    # Atualização considerando cada vértice como intermediário.
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# Exemplo de uso:
vertices = ['A', 'B', 'C', 'D']
grafo_exemplo = {
    'A': {'B': 5, 'C': 10},
    'B': {'C': 3, 'D': 2},
    'C': {'D': 1},
    'D': {}
}

menores_caminhos = floyd_warshall(vertices, grafo_exemplo)

print("Matriz de menores tempos de deslocamento:")
for origem in vertices:
    for destino in vertices:
        print(f"{origem} -> {destino}: {menores_caminhos[origem][destino]}")
    print()
