import networkx  as nx

from utils import open_test_file, close_test_file, get_line
from solve import solve_dsat_coloring

# Para redirigir entrada en local, asigna nombre de fichero.
# test_file = "test1.txt"
test_file = None
input_source = open_test_file(test_file)

first_line = get_line(input_source).split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])

graph = nx.Graph()
graph.add_nodes_from(range(1,num_nodes+1))

for j in range(1, num_edges+1):
        parts = get_line(input_source).split()
        u = int(parts[0])
        v = int(parts[1])
        graph.add_edge(u, v)

order_nodes = graph.nodes()
colores_nodos = solve_dsat_coloring(graph, order_nodes)

print(colores_nodos)

close_test_file(test_file, input_source)