import minigraph as nx


def solve(input_list):
    """Implementa la búsqueda de todas las rutas válidas de start a end.

    input_list: lista de conexiones, por ejemplo ['start-A', 'A-end'].
    Las cuevas pequeñas solo pueden visitarse una vez por ruta.
    Las cuevas grandes pueden visitarse varias veces.

    Devuelve (num_solutions, solutions_list): el número de rutas y una
    lista de rutas, cada una representada como una lista de nombres de cuevas.
    No imprimas los resultados; main.py se encarga de ordenarlos y mostrarlos.
    """
    
    num_solutions = 0
    solutions_list = []

    clean_input = []

    for input in input_list:
        clean_input.append(input.strip().split("-"))

    graph:nx.Graph = nx.Graph()

    for edge in clean_input:
        graph.add_edge(edge[0], edge[1])

    def dfs(solution:list):
        if solution[-1] == 'end':
            solutions_list.append(solution)
            return

        for neighbor in graph.neighbors(solution[-1]):
            if neighbor in solution and neighbor.islower():
                continue
            else:
                solution_copy = solution.copy()
                solution_copy.append(neighbor)
                dfs(solution_copy)

    dfs(['start'])

    return len(solutions_list), solutions_list
