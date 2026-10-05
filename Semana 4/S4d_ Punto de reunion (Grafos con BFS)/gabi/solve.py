from simple_queue import Queue
from sys import maxsize as inf
import minigraph as nx


def solve_punto_reunion(graph:nx.Graph, positions):
    """Completa el cálculo del punto de reunión usando búsquedas BFS con Queue.

    graph: minigraph.Graph no dirigido, sin pesos, con vértices 1..N.
    positions: lista no vacía de posiciones de las personas. Puede contener
    repeticiones porque varias personas pueden partir del mismo vértice.

    Devuelve (punto, distancia_maxima), una tupla de dos enteros:
    - punto: vértice alcanzable por todos que minimiza la mayor distancia
      desde las posiciones. En empate elige el menor identificador numérico.
    - distancia_maxima: valor de esa mayor distancia, en número de aristas.
    Si no existe un punto común alcanzable, devuelve (-1, -1).

    Realiza BFS desde cada posición distinta usando Queue como cola FIFO.
    También se admite repetir BFS para personas con la misma posición.
    Considera todos los vértices como candidatos, incluidas las posiciones
    iniciales. No minimices la suma de distancias. Una única BFS multiorigen
    no proporciona las distancias individuales necesarias para este criterio.

    No modifiques los parámetros ni leas ni imprimas. main.py ya lee los
    datos, construye el grafo y presenta el resultado. Entradas válidas.
    Se proporcionan minigraph.py y simple_queue.py completos.
    """
    distances = []

    def bfs(position):
        distance = {}
        for node in graph.nodes():
            distance[node] = inf

        queue:Queue = Queue()
        visibles = set()
        visibles.add(position)

        queue.enqueue(position)
        distance[position] = 0

        while queue.isEmpty() == False:
            node = queue.dequeue()
            for edge in graph.neighbors(node):
                if edge not in visibles:
                    visibles.add(edge)
                    distance[edge] = distance[node] + 1
                    queue.enqueue(edge)
        return distance

    for position in positions:
        distances.append(bfs(position))
        print(distances)

    i = 0
    candidates = []
    while i < graph.number_of_nodes():
        ...

            

