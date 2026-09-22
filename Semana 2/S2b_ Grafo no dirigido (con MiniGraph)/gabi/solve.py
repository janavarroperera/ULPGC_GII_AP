import minigraph as nx


def build_graph(edges_list, num_nodes, num_edges):
    """
    Construye y devuelve un grafo no dirigido a partir de una lista de aristas.

    Parámetros:
        edges_list: lista de cadenas con las aristas del grafo.
            Cada cadena tiene el formato "u v", donde u y v son enteros.
            Ejemplo: ["1 4", "2 8", "3 6"]

        num_nodes: número total de vértices del grafo.
            Los vértices deben numerarse desde 1 hasta num_nodes.

        num_edges: número total de aristas del grafo.
            Coincide con el número de líneas contenidas en edges_list.

    Debe devolver:
        Un objeto nx.Graph() que contenga todos los vértices y todas las
        aristas indicadas en la entrada.

    Restricciones:
        - No leer de teclado ni de ficheros en esta función.
        - No imprimir nada en esta función.
        - No modificar main.py.
        - Usar nx.Graph(), add_node() y add_edge().
    """

    # Crea aquí un grafo no dirigido con nx.Graph().
    graph = nx.Graph()

    # Añade aquí todos los vértices desde 1 hasta num_nodes.
    i = 0
    while i < num_nodes:
        graph.add_node(i+1)
        i += 1

    # Recorre edges_list, separa cada línea en dos extremos u y v,
    # conviértelos a enteros y añade la arista correspondiente.

    # Devuelve el grafo construido.


    for edge in edges_list:
        graph.add_edge(int(edge[0]), int(edge[2]))

    return graph
