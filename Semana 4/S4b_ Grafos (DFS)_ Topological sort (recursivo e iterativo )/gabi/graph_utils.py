import minigraph as nx


def build_digraph_with_weights(edges_list, num_nodes, num_edges):
    """Construye y devuelve un grafo dirigido con pesos usando MiniGraph.

    Parámetros:
        edges_list: lista de num_edges cadenas con formato "origen destino peso".
        num_nodes: número de vértices, numerados desde 1 hasta num_nodes.
        num_edges: número de aristas descritas en edges_list.

    Devuelve:
        Un objeto nx.DiGraph con todos los vértices, incluidos los aislados,
        y las aristas dirigidas con sus pesos enteros en el atributo weight.

    La función no debe leer datos ni imprimir resultados.
    """
    graph:nx.DiGraph = nx.DiGraph()

    i = 0

    while i < num_nodes:
        graph.add_node(i+1)
        i += 1

    cleaned_edges = []

    for edge in edges_list:
        cleaned_edges.append(edge.strip().split())

    for edge in cleaned_edges:
        graph.add_edge(int(edge[0]), int(edge[1]), int(edge[2]))

    return graph