import heapq

def prim_telefonia(grafo, inicio):
    """
    grafo: dicionário onde cada chave é uma torre e o valor é uma lista de tuplas (torre vizinha, custo_conexao).
    inicio: torre escolhida para iniciar a construção da rede de comunicação.
    
    Retorna uma tupla (conexoes, custo_total) onde:
      - conexoes é uma lista de arestas no formato (torre_origem, torre_destino, custo_conexao).
      - custo_total é a soma dos custos de conexão selecionados.
    """
    visitados = set()
    conexoes = []
    custo_total = 0
    fila = [(0, inicio, None)]  # (custo, torre_atual, torre_origem)

    while fila and len(visitados) < len(grafo):
        custo, torre, origem = heapq.heappop(fila)
        if torre in visitados:
            continue
        visitados.add(torre)
        if origem is not None:
            conexoes.append((origem, torre, custo))
            custo_total += custo
        for vizinho, custo_aresta in grafo[torre]:
            if vizinho not in visitados:
                heapq.heappush(fila, (custo_aresta, vizinho, torre))
                
    return conexoes, custo_total

# Exemplo de uso:
grafo_torres = {
    'T1': [('T2', 4), ('T3', 3)],
    'T2': [('T1', 4), ('T3', 2), ('T4', 7)],
    'T3': [('T1', 3), ('T2', 2), ('T4', 5)],
    'T4': [('T2', 7), ('T3', 5)]
}

conexoes, custo_total = prim_telefonia(grafo_torres, 'T1')
print("Conexões mínimas para a rede de telefonia:")
for origem, destino, custo in conexoes:
    print(f"{origem} - {destino}: {custo}")
print("Custo total:", custo_total)
