import heapq

def prim(grafo, inicio):
    """
    grafo: dicionário onde cada chave é uma cidade e o valor é uma lista de tuplas (cidade_vizinha, custo_conexao).
    inicio: cidade escolhida para iniciar a construção da árvore.
    
    Retorna uma tupla (arvore, custo_total) onde:
      - arvore é uma lista de conexões no formato (cidade_origem, cidade_destino, custo).
      - custo_total é a soma dos custos das conexões selecionadas.
    """
    visitados = set()
    arvore = []
    custo_total = 0
    fila = [(0, inicio, None)]  # (custo, cidade_atual, cidade_origem)

    while fila and len(visitados) < len(grafo):
        custo, cidade, origem = heapq.heappop(fila)
        if cidade in visitados:
            continue
        visitados.add(cidade)
        if origem is not None:
            arvore.append((origem, cidade, custo))
            custo_total += custo
        for vizinho, custo_aresta in grafo[cidade]:
            if vizinho not in visitados:
                heapq.heappush(fila, (custo_aresta, vizinho, cidade))
                
    return arvore, custo_total

# Exemplo de uso:
grafo_cidades = {
    'CityA': [('CityB', 10), ('CityC', 15)],
    'CityB': [('CityA', 10), ('CityC', 8), ('CityD', 12)],
    'CityC': [('CityA', 15), ('CityB', 8), ('CityD', 6)],
    'CityD': [('CityB', 12), ('CityC', 6)]
}

arvore, custo_total = prim(grafo_cidades, 'CityA')
print("Árvore Geradora Mínima:")
for origem, destino, custo in arvore:
    print(f"{origem} - {destino}: {custo}")
print("Custo total:", custo_total)
