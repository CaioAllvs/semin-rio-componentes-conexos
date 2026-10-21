def dfs(grafo, vertice, visitados, componente):
    visitados.add(vertice)          # Marca como visitado
    componente.append(vertice)      # Adiciona ao grupo atual

    for vizinho in grafo[vertice]:  # Percorre os vizinhos
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados, componente)


def encontrar_componentes(grafo):
    visitados = set()   # Guarda quem já foi visitado
    componentes = []    # Guarda todos os grupos

    for vertice in grafo:
        if vertice not in visitados:
            componente = []         # Novo componente

            dfs(grafo, vertice, visitados, componente)

            componentes.append(componente)

    return componentes


grafo = {
    "Aeroporto": ["Centro", "Porto", "Vice City"],
    "Centro": ["Aeroporto", "Bairro Norte", "Vice City"],
    "Bairro Norte": ["Centro", "Universidade", "Praia Central"],
    "Universidade": ["Bairro Norte", "Área Comercial"],
    "Porto": ["Aeroporto", "Vice City", "Ilha das Docas"],
    "Vice City": ["Aeroporto", "Centro", "Porto", "Praia Central", "Ilha Oeste"],
    "Praia Central": ["Bairro Norte", "Vice City", "Área Comercial", "Ilha Leste"],
    "Área Comercial": ["Universidade", "Praia Central", "Subúrbio"],
    "Subúrbio": ["Área Comercial"],
    "Ilha das Docas": ["Porto", "Ilha Oeste"],
    "Ilha Oeste": ["Ilha das Docas", "Vice City", "Ilha Leste", "Ilha Sul"],
    "Ilha Leste": ["Praia Central", "Ilha Oeste", "Ilha Sul"],
    "Ilha Sul": ["Ilha Oeste", "Ilha Leste"],

    "Montanha": ["Floresta", "Base Secreta"],
    "Floresta": ["Montanha", "Base Secreta"],
    "Base Secreta": ["Montanha", "Floresta"],

    "Ilha Militar": ["Ilha de Pesquisa", "Ilha Restrita"],
    "Ilha de Pesquisa": ["Ilha Militar", "Ilha Restrita"],
    "Ilha Restrita": ["Ilha Militar", "Ilha de Pesquisa"]
}


# Executa o algoritmo
componentes = encontrar_componentes(grafo)


# Mostra quantos grupos existem
print("Quantidade de componentes conexos:", len(componentes))
print()


# Mostra cada componente
for i, componente in enumerate(componentes, start=1):
    print(f"Componente {i}: {componente}")