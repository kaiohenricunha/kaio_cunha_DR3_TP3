import heapq

def prim(grafo, inicio):
    """
    grafo: dicionário onde cada chave é um vértice e o valor é uma lista de tuplas (vértice, peso).
    inicio: vértice de partida para formar a Árvore Geradora Mínima.
    
    Retorna uma tupla (arvore, custo_total) onde:
      - arvore é uma lista de arestas no formato (vértice1, vértice2, peso).
      - custo_total é a soma dos pesos das arestas da árvore.
    """
    visitados = set()
    arvore = []
    custo_total = 0
    fila = [(0, inicio, None)]  # (peso, vértice, vértice_origem)

    while fila and len(visitados) < len(grafo):
        peso, vertice, origem = heapq.heappop(fila)
        if vertice in visitados:
            continue
        visitados.add(vertice)
        if origem is not None:
            arvore.append((origem, vertice, peso))
            custo_total += peso
        for vizinho, custo in grafo[vertice]:
            if vizinho not in visitados:
                heapq.heappush(fila, (custo, vizinho, vertice))
                
    return arvore, custo_total

# Exemplo de uso:
grafo_exemplo = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('C', 8), ('H', 11)],
    'C': [('B', 8), ('D', 7), ('F', 4), ('I', 2)],
    'D': [('C', 7), ('E', 9), ('F', 14)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('H', 1), ('I', 6)],
    'H': [('A', 8), ('B', 11), ('G', 1), ('I', 7)],
    'I': [('C', 2), ('G', 6), ('H', 7)]
}

arvore, custo_total = prim(grafo_exemplo, 'A')
print("Árvore Geradora Mínima:")
for origem, destino, peso in arvore:
    print(f"{origem} - {destino} : {peso}")
print("Custo total:", custo_total)
