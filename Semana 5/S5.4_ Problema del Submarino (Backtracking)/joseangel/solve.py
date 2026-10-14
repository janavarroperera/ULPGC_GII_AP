import minigraph as nx


def solve(input_list):


    """FUNCOIN RECURSIVA DFS"""
    def dfs(solution):
        if solution[-1] == "end":
            solutions_list.append(solution)
            return


        for neighbor in G.neighbors(solution[-1]):
            new_solution = solution.copy()
            if (neighbor.islower() and neighbor in solution) or (neighbor == "start"):
                continue
            new_solution.append(neighbor)
            dfs(new_solution)
        return

        
        

    solutions_list = []

    # print(input_list)
    
    """LIMPIAR EL IMPUT"""
    edge_list = []
    for edge in input_list:
        if edge[-1] == '\r':
            edge_list.append(edge[:-1])
        else:
            edge_list.append(edge)
    # print(edge_list)


    """CREAR EL GRAFO"""
    G = nx.Graph()
    for edge in edge_list:
        edge = edge.split("-")
        G.add_edge(edge[0], edge[1])
    # print(G.edges())

    first_step = ["start"]

    dfs(first_step)


    


    

    return len(solutions_list), solutions_list
