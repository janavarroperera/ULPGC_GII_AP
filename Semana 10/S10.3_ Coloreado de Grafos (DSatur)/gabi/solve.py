import networkx as nx


# [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 6)]
def solve_dsat_coloring(graph:nx.Graph, order_nodes):
    
    # Implementación del algoritmo DSatur
    nodes_colors = {}
    saturations = {}
    for node in order_nodes:
        nodes_colors[node] = None
        saturations[node] = 0

    # Escribir el código a partir de aquí
    # _____________________________________________________________________
    #Se le da al nodo con mayor grado un color
    first_node = [-1, -1]
    for node in graph.nodes():
        if graph.degree(node) > first_node[1]:
            first_node = [node, graph.degree(node)]
    nodes_colors[first_node[0]] = 0

    for node in graph.neighbors(first_node[0]):
        saturations[node] = 1

    # Exploramos las saturaciones

    colored = 1

    while colored != len(nodes_colors):
        next_node = [-1, -1]
        for node in graph.nodes():
            if nodes_colors[node] == None:
                if next_node == [-1, -1]:
                    next_node = [node, graph.degree(node)]
                    continue
                if saturations[node] >= saturations[next_node[0]]:
                    if saturations[node] == saturations[next_node[0]]:
                        # Si la saturación es igual se comprueban los grados
                        if graph.degree(node) > graph.degree(next_node[0]):
                            next_node = [node, graph.degree(node)]
                        elif graph.degree(node) == graph.degree(next_node[0]):
                            if node < next_node[0]:
                                next_node = [node, graph.degree(node)]
                    else:
                        next_node = [node, graph.degree(node)]

        # Se le asigna un color distinto
        used_colors = set()
        for neighbor in graph.neighbors(next_node[0]):
            if nodes_colors[neighbor] != None:
                used_colors.add(nodes_colors[neighbor])
        color = 0
        while color in used_colors:
            color += 1
        nodes_colors[next_node[0]] = color
        colored += 1

        # Calculo de saturaciones:
        for nodes in graph.nodes():
            seen_colors = set()
            for neighbor in graph.neighbors(node):
                if nodes_colors[neighbor] != None:
                    seen_colors.add(nodes_colors[neighbor])
            saturations[nodes] = len(seen_colors)


    # _____________________________________________________________________

    return [nodes_colors[node] for node in order_nodes]

