import heapq

def dijkstra_airports(grafo, origem, destino):
    distancias = {aeroporto: float('inf') for aeroporto in grafo}
    predecessores = {aeroporto: None for aeroporto in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]
    
    while fila:
        distancia_atual, aeroporto = heapq.heappop(fila)
        if aeroporto == destino:
            break
        if distancia_atual > distancias[aeroporto]:
            continue
        for vizinho, distancia in grafo[aeroporto]:
            nova_dist = distancia_atual + distancia
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                predecessores[vizinho] = aeroporto
                heapq.heappush(fila, (nova_dist, vizinho))
    
    # Reconstrução do trajeto
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    return distancias[destino], caminho

grafo_aeroportos = {
    'JFK': [('ATL', 760), ('ORD', 740)],
    'ATL': [('JFK', 760), ('LAX', 1940)],
    'ORD': [('JFK', 740), ('LAX', 1744)],
    'LAX': [('ATL', 1940), ('ORD', 1744)]
}

distancia, rota = dijkstra_airports(grafo_aeroportos, 'JFK', 'LAX')
print("Distância mínima:", distancia)
print("Rota:", rota)
