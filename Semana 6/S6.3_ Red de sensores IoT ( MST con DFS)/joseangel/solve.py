import minigraph as nx
import copy 
import simple_stack as stack

def tiene_camino(arbol, edge):
  pila = stack.Stack()

 

  visitados = [edge[0]]
  pila.push(edge[0])

  while pila.isEmpty() is False:
    nodo = pila.pop()
    for neighbor in arbol.neighbors(nodo):
      if neighbor not in visitados:
        visitados.append(neighbor)
        pila.push(neighbor)

  if edge[1] in visitados:
    return True
  else:
    return False

def kruskal_mst_dfs(G):
  ordered_edges = G.edges().copy()

  ordered_edges = sorted(ordered_edges, key = lambda edge: edge[2])

  arbol = nx.Graph()

  mst = []
  mst_length = 0

  for edge in ordered_edges:
    if tiene_camino(arbol, edge) == True:
      continue
    arbol.add_edge(edge[0], edge[1], edge[2])
    a, b = min(edge[0], edge[1]), max(edge[0], edge[1])
    mst.append((a, b, edge[2]))
    mst_length += edge[2]

  print(arbol.edges())

  if len(mst) != len(G.nodes()) - 1:
    return None

  total_length = sum(edge[2] for edge in ordered_edges)


  return mst, mst_length, total_length
