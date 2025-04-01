import heapq

def dijkstra(grafo, origem):
    distancias = {v: float('inf') for v in grafo}
    distancias[origem] = 0
    visitados = set()
    fila = [(0, origem)]

    while fila:
        dist_atual, vertice = heapq.heappop(fila)
        if vertice in visitados:
            continue
        visitados.add(vertice)

        for vizinho, custo in grafo[vertice]:
            nova_dist = dist_atual + custo
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias

grafo_exemplo = {
    'Centro': [('Bairro1', 4), ('Bairro2', 2)],
    'Bairro1': [('Centro', 4), ('Bairro3', 1)],
    'Bairro2': [('Centro', 2), ('Bairro3', 5)],
    'Bairro3': [('Bairro1', 1), ('Bairro2', 5)]
}

menores_distancias = dijkstra(grafo_exemplo, 'Centro')
print(menores_distancias)
