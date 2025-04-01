import heapq

def prim_abastecimento(grafo, inicio):
    """
    grafo: dicionário onde cada chave é um bairro e o valor é uma lista de tuplas (bairro_vizinho, custo_instalacao).
    inicio: bairro escolhido para iniciar a construção do sistema de abastecimento.
    
    Retorna uma tupla (plano_instalacao, custo_total) onde:
      - plano_instalacao é uma lista de conexões no formato (bairro_origem, bairro_destino, custo).
      - custo_total é a soma dos custos das tubulações selecionadas.
    """
    visitados = set()
    plano_instalacao = []
    custo_total = 0
    fila = [(0, inicio, None)]  # (custo, bairro_atual, bairro_origem)

    while fila and len(visitados) < len(grafo):
        custo, bairro, origem = heapq.heappop(fila)
        if bairro in visitados:
            continue
        visitados.add(bairro)
        if origem is not None:
            plano_instalacao.append((origem, bairro, custo))
            custo_total += custo
        for vizinho, custo_aresta in grafo[bairro]:
            if vizinho not in visitados:
                heapq.heappush(fila, (custo_aresta, vizinho, bairro))
                
    return plano_instalacao, custo_total

# Exemplo de uso:
grafo_bairros = {
    'Bairro1': [('Bairro2', 7), ('Bairro3', 9), ('Bairro4', 14)],
    'Bairro2': [('Bairro1', 7), ('Bairro3', 10), ('Bairro4', 15)],
    'Bairro3': [('Bairro1', 9), ('Bairro2', 10), ('Bairro4', 11)],
    'Bairro4': [('Bairro1', 14), ('Bairro2', 15), ('Bairro3', 11)]
}

plano, custo_total = prim_abastecimento(grafo_bairros, 'Bairro1')
print("Plano de instalação:")
for origem, destino, custo in plano:
    print(f"{origem} - {destino} : {custo}")
print("Custo total:", custo_total)
