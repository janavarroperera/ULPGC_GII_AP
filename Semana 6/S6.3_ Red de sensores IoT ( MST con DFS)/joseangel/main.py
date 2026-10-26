from utils import open_test_file, close_test_file, get_line
from minigraph import MiniGraph
from solve import kruskal_mst_dfs

TEST_FILE = "test.txt" 

def read_tokens(source):
    # Lee la siguiente línea no vacía como lista de tokens
    while True:
        line = get_line(source)
        if line is None:
            return None
        line = line.strip()
        if line:
            return line.split()

inp = open_test_file(TEST_FILE)

try:
    # Primera línea: N M
    tokens = read_tokens(inp)
    N, M = int(tokens[0]), int(tokens[1])

    # Segunda línea: nombres de nodos (incluye 'MCU' como coordinador)
    names = read_tokens(inp)

    G = MiniGraph()
    for name in names:
        G.add_node(name)

    # M líneas de aristas u v w (grafo no dirigido)
    for _ in range(M):
        t = read_tokens(inp)
        u, v, w = t[0], t[1], int(t[2])
        # aristas no dirigidas
        G.add_edge(u, v, w, None, False)

    res = kruskal_mst_dfs(G)
    if res is None:
        print("NO_MST", end="")
    else:
        mst, mst_length, total_length = res
        print("MST:")
        for (u, v, w) in mst:
            print(f"{u} {v} {w}")
        print(f"MST_length={mst_length}")
        # Última línea sin salto final; longitudes expresadas en metros
        print(f"Total_length={total_length}", end="")

finally:
    close_test_file(TEST_FILE, inp)
