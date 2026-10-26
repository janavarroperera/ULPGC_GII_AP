import minigraph as nx
import copy 

def tiene_bucle(arbol):
  pass

def kruskal_mst_dfs(G):
  # print(G.edges())

  ordered_edges = G.edges().copy()

  ordered_edges = sorted(ordered_edges, key = lambda edge: edge[2])

  # print(ordered_edges)

  arbol_temporal = nx.Graph()
  arbol_temporal.add_node(ordered_edges[0][0])

  arbol_final = copy.deepcopy(arbol_temporal)

  for edge in ordered_edges[1:]:
    arbol_temporal.add_edge(edge)
    if tiene_bucle(arbol_temporal) == True:
      arbol_temporal = copy.deepcopy(arbol_final)
      continue
    arbol_final.add_edge(edge)
    arbol_temporal = copy.deepcopy(arbol_final)
    


  return
