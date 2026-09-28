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
from solve import *

first_line = get_line(input_source).split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
edges_list = get_n_lines(input_source, num_edges)

graph = build_digraph_with_weights(edges_list, num_nodes, num_edges)

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges(data=True))


# --------------------------------------------------------------------
# Close the file if it was opened
if test_file is not None:
    input_source.close()