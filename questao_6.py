import heapq

def dijkstra_internacional(grafo, origem, destino, tempo_max_conexao):
    """
    grafo: dicionário onde cada chave é um aeroporto e cada valor é uma lista de tuplas:
           (destino, custo_voo, tempo_conexao, custo_escalas)
           - custo_voo: custo base do voo (inclui taxas e impostos).
           - tempo_conexao: tempo necessário para a conexão (apenas para aeroportos intermediários).
           - custo_escalas: custo adicional fixo se houver escala obrigatória.
    origem: aeroporto de partida.
    destino: aeroporto de chegada.
    tempo_max_conexao: tempo máximo permitido para conexões em aeroportos intermediários.
    
    Retorna uma tupla com (custo_total, rota), onde 'rota' é a sequência de aeroportos percorridos.
    """
    distancias = {aeroporto: float('inf') for aeroporto in grafo}
    predecessores = {aeroporto: None for aeroporto in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]
    
    while fila:
        custo_atual, aeroporto = heapq.heappop(fila)
        if aeroporto == destino:
            break
        if custo_atual > distancias[aeroporto]:
            continue
        for vizinho, custo_voo, tempo_conexao, custo_escalas in grafo[aeroporto]:
            # Para o primeiro voo, não se aplica restrição de conexão.
            if aeroporto != origem and tempo_conexao > tempo_max_conexao:
                continue
            custo_total_voo = custo_voo + custo_escalas
            novo_custo = custo_atual + custo_total_voo
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                predecessores[vizinho] = aeroporto
                heapq.heappush(fila, (novo_custo, vizinho))
    
    if distancias[destino] == float('inf'):
        return float('inf'), []
    
    # Reconstrução da rota a partir dos predecessores.
    rota = []
    atual = destino
    while atual is not None:
        rota.append(atual)
        atual = predecessores[atual]
    rota.reverse()
    
    return distancias[destino], rota

grafo_voos = {
    'JFK': [('LHR', 500, 0, 0), ('CDG', 550, 0, 50)],  # Origem: não há tempo de conexão
    'LHR': [('DXB', 600, 2, 0), ('FRA', 200, 1, 20)],
    'CDG': [('DXB', 650, 3, 0), ('FRA', 180, 0.5, 0)],
    'FRA': [('DXB', 550, 2, 0)],
    'DXB': []
}

tempo_max_conexao = 2.5  # Limite de tempo para conexões (horas)
custo, rota = dijkstra_internacional(grafo_voos, 'JFK', 'DXB', tempo_max_conexao)
print("Custo total:", custo)
print("Rota:", rota)
