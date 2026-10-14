def kruskal_mst_dfs(G):
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

    return
