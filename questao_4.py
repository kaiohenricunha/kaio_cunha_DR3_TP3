import heapq

def dijkstra_transporte(grafo, origem, destino):
    distancias = {cidade: float('inf') for cidade in grafo}
    predecessores = {cidade: None for cidade in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]
    
    while fila:
        custo_atual, cidade = heapq.heappop(fila)
        if cidade == destino:
            break
        if custo_atual > distancias[cidade]:
            continue
        for vizinho, custo in grafo[cidade]:
            novo_custo = custo_atual + custo
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                predecessores[vizinho] = cidade
                heapq.heappush(fila, (novo_custo, vizinho))
    
    # Reconstrução do caminho
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    return distancias[destino], caminho

grafo_cidades = {
    'CidadeA': [('CidadeB', 50), ('CidadeC', 100)],
    'CidadeB': [('CidadeA', 50), ('CidadeC', 40), ('CidadeD', 70)],
    'CidadeC': [('CidadeA', 100), ('CidadeB', 40), ('CidadeD', 60)],
    'CidadeD': [('CidadeB', 70), ('CidadeC', 60)]
}

custo_min, rota = dijkstra_transporte(grafo_cidades, 'CidadeA', 'CidadeD')
print("Custo mínimo:", custo_min)
print("Rota:", rota)
