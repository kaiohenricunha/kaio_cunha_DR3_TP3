import heapq

def dijkstra_caminho(grafo, origem, destino):
    distancias = {v: float('inf') for v in grafo}
    predecessores = {v: None for v in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]

    while fila:
        tempo_atual, vertice = heapq.heappop(fila)
        if tempo_atual > distancias[vertice]:
            continue
        if vertice == destino:
            break
        for vizinho, tempo in grafo[vertice]:
            novo_tempo = tempo_atual + tempo
            if novo_tempo < distancias[vizinho]:
                distancias[vizinho] = novo_tempo
                predecessores[vizinho] = vertice
                heapq.heappush(fila, (novo_tempo, vizinho))
    
    # Reconstrução do caminho
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    return distancias[destino], caminho

grafo_exemplo = {
    'A': [('B', 5), ('C', 10)],
    'B': [('A', 5), ('C', 3), ('D', 2)],
    'C': [('A', 10), ('B', 3), ('D', 1)],
    'D': [('B', 2), ('C', 1)]
}

tempo, percurso = dijkstra_caminho(grafo_exemplo, 'A', 'D')
print("Tempo mínimo:", tempo)
print("Percurso:", percurso)
