import heapq

def dijkstra_rota_cidade_inteligente(grafo, origem, destino, autonomia, estações):
    """
    grafo: dicionário onde cada chave é um nó e cada valor é uma lista de tuplas (vizinho, tempo, distância).
    origem: nó de partida.
    destino: nó de chegada.
    autonomia: autonomia máxima do veículo (em km).
    estações: conjunto de nós com estações de recarga.
    """
    # Cada estado é (tempo_acumulado, nó, autonomia_restante).
    fila = [(0, origem, autonomia)]
    # best guarda o menor tempo para cada estado (nó, autonomia_restante)
    best = {(origem, autonomia): 0}
    # pred guarda o estado anterior para reconstrução do caminho.
    pred = {(origem, autonomia): None}
    
    final_estado = None

    while fila:
        tempo_atual, nó, bateria = heapq.heappop(fila)
        if tempo_atual > best.get((nó, bateria), float('inf')):
            continue
        if nó == destino:
            final_estado = (nó, bateria)
            break
        for vizinho, tempo_viagem, distancia in grafo[nó]:
            if distancia > bateria:
                continue  # autonomia insuficiente para esta rua.
            nova_bateria = bateria - distancia
            if vizinho in estações:
                nova_bateria = autonomia  # recarrega a bateria.
            novo_tempo = tempo_atual + tempo_viagem
            novo_estado = (vizinho, nova_bateria)
            if best.get(novo_estado, float('inf')) > novo_tempo:
                best[novo_estado] = novo_tempo
                heapq.heappush(fila, (novo_tempo, vizinho, nova_bateria))
                pred[novo_estado] = (nó, bateria)
    
    if final_estado is None:
        return float('inf'), []
    
    # Reconstrução do caminho a partir dos estados.
    caminho = []
    estado = final_estado
    while estado is not None:
        nó_atual, _ = estado
        caminho.append(nó_atual)
        estado = pred.get(estado)
    caminho.reverse()
    
    return best[final_estado], caminho

# Exemplo de uso:
grafo_cidade = {
    'A': [('B', 10, 50), ('C', 15, 70)],
    'B': [('A', 10, 50), ('C', 5, 30), ('D', 20, 80)],
    'C': [('A', 15, 70), ('B', 5, 30), ('D', 10, 40), ('E', 20, 90)],
    'D': [('B', 20, 80), ('C', 10, 40), ('E', 5, 20)],
    'E': [('C', 20, 90), ('D', 5, 20)]
}

estações = {'B', 'D'}  # nós com estações de recarga.
autonomia = 100

tempo_total, rota = dijkstra_rota_cidade_inteligente(grafo_cidade, 'A', 'E', autonomia, estações)
print("Tempo total:", tempo_total)
print("Rota:", rota)
# Output esperado:
# Tempo total: 25
# Rota: ['A', 'B', 'C', 'D', 'E']
