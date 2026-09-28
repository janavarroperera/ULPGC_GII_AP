import minigraph as nx
from solve import solve_punto_reunion
from utils import open_test_file, close_test_file, get_line


test_file = None
input_source = open_test_file(test_file)

try:
    n, m, k = map(int, get_line(input_source).split())
    positions = list(map(int, get_line(input_source).split()))
    graph = nx.Graph()
    for u in range(1, n + 1):
        graph.add_node(u)
    for _ in range(m):
        u, v = map(int, get_line(input_source).split())
        graph.add_edge(u, v)
    point, radius = solve_punto_reunion(graph, positions)
    print(f'Punto={point}')
    print(f'DistanciaMaxima={radius}')
finally:
    close_test_file(test_file, input_source)


