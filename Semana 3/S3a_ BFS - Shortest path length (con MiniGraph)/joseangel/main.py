# -----------------------------------------------------------------
# Para redireccionar la entrada en Wing 101 crea un fichero con
# los datos de entrada en la misma carpeta donde tienes el fichero
# main.py de este ejercicio y añade aquí una string con el nombre
# del fichero.
#    Ejemplo:
#    test_file = "test1.txt"

from utils import *

test_file    = None
input_source = open_test_file (test_file)

# ----------------------------------------------------------------
import minigraph as nx
from graph_utils import *
from solve import *

first_line = input_source.readline().split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
edges_list = get_n_lines(input_source, num_edges)

# Añade al fichero graph_utils.py tu función para crear un
# grafo no dirigido sin pesos
graph = build_graph(edges_list, num_nodes, num_edges);

first_node = 1
distances = bfs_path_length(graph, first_node)
ordered_distances = dict(sorted(distances.items()))
print(ordered_distances)

# --------------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)
