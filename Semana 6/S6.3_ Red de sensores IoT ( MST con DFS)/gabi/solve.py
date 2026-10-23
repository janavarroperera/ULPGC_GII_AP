import minigraph as nx
import copy

def kruskal_mst_dfs(G:nx.Graph):
    """
    Calcula MST con Kruskal detectando ciclos mediante DFS en grafo parcial.

    Parámetros
    ----------
    G : minigraph.MiniGraph
        Grafo no dirigido ponderado que devuelve:
        - `G.nodes()` lista de pares (nodeid, data).
        - `G.edges()` tuplas (u, v, label, data, directed), con `label` = longitud en metros.

    Retorna
    -------
    tuple | None
        (mst_edges, mst_length, total_length) si grafo es conexo y existe MST.
        None si el grafo no es conexo.

    Detalles de implementación
    --------------------------
    - Orden determinista: ordenar aristas por (w, a, b), con `a <= b`.
    - Detección de ciclo: antes de añadir arista (u, v, w),
      realizar DFS sobre grafo PARCIAL y si ya hay camino u->v,
      descartar arista para evitar ciclo.
    - Al añadir al MST, registrar (a, b, w) con `a <= b` y w en metros.
    - Devolver también `mst_length` (longitud total del cable del MST)
      y `total_length` (suma de las longitudes de todas las conexiones del grafo),
      ambas en metros.

    Nota
    ----
    - La lectura de entrada y la generación de la salida exacta
      las gestiona `main.py`.
    """

    def get_weight(edge):
        return edge[2]

    edges = []
    length = 0
    total_length = 0

    for edge in G.edges():
        total_length += edge[2]
        edges.append(edge)
    edges.sort(key=get_weight)

    total_solutions = []

    def path_exist(graph:nx.Graph, destination, solution:list):
        if solution[-1] == destination:
            total_solutions.append(solution)
            return

        for neighbor in graph.neighbors(solution[-1]):
            if neighbor in solution:
                continue
            solution_copy = solution.copy()
            solution_copy.append(neighbor)
            path_exist(graph, destination, solution_copy)

    mst:nx.Graph = nx.Graph()


    for edge in edges:
        mst_copy = copy.deepcopy(mst)
        mst_copy.add_edge(edge[0], edge[1], edge[2])
        total_solutions.clear()
        path_exist(mst_copy, edge[1], [edge[0]])

        if len(total_solutions) > 1:
            continue
        else:
            length += edge[2]
            mst.add_edge(edge[0], edge[1], weight=edge[2])

    if mst.number_of_nodes() != len(G.nodes()):
        return None
    
    return mst.edges(data=True), length, total_length
