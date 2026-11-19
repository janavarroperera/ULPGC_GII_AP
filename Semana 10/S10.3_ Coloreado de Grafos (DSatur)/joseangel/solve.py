import networkx as nx


def solve_dsat_coloring(graph, order_nodes):

    
    def saturacion(node):
        sat = 0
        contados = []
        neighbors = graph.neighbors(node)
        for neighbor in neighbors:
            if (nodes_colors[neighbor] is not None) and (nodes_colors[neighbor] not in contados):
                contados.append(nodes_colors[neighbor])
                sat += 1
        return sat


    # Implementación del algoritmo DSatur
    nodes_colors = {}
    pendientes = []
    for node in order_nodes:
        nodes_colors[node] = None
        pendientes.append(node)
    

    while pendientes:
        mayor_sat = pendientes[0]
        for node in pendientes:
            if saturacion(node) > saturacion(mayor_sat):
                mayor_sat = node
            elif saturacion(node) == saturacion(mayor_sat):
                if graph.degree(node) > graph.degree(mayor_sat):
                    mayor_sat = node

        color = 0
        while True:
            for neighbor in graph.neighbors(mayor_sat):
                if nodes_colors[neighbor] == color:
                   color += 1
                   break #repite el bucle
            else:
                nodes_colors[mayor_sat] = color
                break

        pendientes.remove(mayor_sat)



    return [nodes_colors[node] for node in order_nodes]
