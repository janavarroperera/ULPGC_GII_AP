import minigraph  as nx
from sys          import maxsize as infinite
from simple_queue import *


def bfs_path_length(graph:nx.Graph, first_node):
    """
    Calcula las distancias mínimas desde first_node mediante BFS.

    Parámetros:
        graph: grafo no dirigido y sin pesos de MiniGraph.
        first_node: vértice de origen, perteneciente al grafo.

    Devuelve:
        Un diccionario {vertice: distancia_en_aristas} para todos los
        vértices del grafo. La distancia del origen es 0 y la de los
        vértices no alcanzables es infinite (sys.maxsize).

    Utiliza la clase Queue de simple_queue.py.
    No lee entrada ni imprime resultados; main.py gestiona la E/S.
    """


    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite
    # solve it here!
    # ...
    queue = Queue()
    visibles = [graph.nodes()[0]]

    queue.enqueue(graph.nodes()[0])
    distance[1] = 0

    while queue.isEmpty() == False:
        v = queue.dequeue()

        for edge in graph.neighbors(v):
            if edge not in visibles:
                visibles.append(edge)
                distance[edge] = distance[v] + 1
                queue.enqueue(edge)

    return distance
