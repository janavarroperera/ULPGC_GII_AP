from simple_queue import Queue


def solve_punto_reunion(graph, positions):

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
  punto = (-1, -1) 
  distances_list = []
  candidates = graph.nodes()

  for pos in set(positions):
    distances_list.append(bfs(graph, pos))

  for node in graph.nodes():
    for dictionary in distances_list:
      if node not in dictionary and node in candidates:
        candidates.remove(node)
        continue

  if candidates == []: return punto

  candidates_max_distance = {}

  for candidate in candidates:
    max_distance = 0
    for dic in distances_list:
      if dic[candidate] > max_distance:
        max_distance = dic[candidate]
    candidates_max_distance[candidate] = max_distance

  punto = min(candidates_max_distance.items(), key=lambda par: par[1])
    
  return punto

def bfs(graph, first_node):
  distance = {}
    
  visibles = []
  queue = Queue()
  visibles.append(first_node)
  queue.enqueue(first_node)
  distance[first_node] = 0

  while queue. isEmpty() == False:
    node = queue.dequeue()
    for neighbor in graph.neighbors(node):
      if neighbor not in visibles:
        visibles.append(neighbor)
        queue.enqueue(neighbor)
        distance[neighbor] = distance[node] + 1


  return distance