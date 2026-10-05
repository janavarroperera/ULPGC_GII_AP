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

    # crea el digrafo
    graph = nx.DiGraph() 

    # añadir nodos
    for i in range(1, num_nodes + 1):
        graph.add_node(i)

    # añadir vertices
    for edge in edges_list:
        edge = edge.split()
        # print(edge[0],edge[1],edge[2][0:-1])
        graph.add_edge(int(edge[0]), int(edge[1]), int(edge[2]))

    return graph
