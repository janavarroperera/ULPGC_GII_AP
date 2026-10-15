from typing import List, Tuple


def solve(
    budget: int,
    items: List[Tuple[str, int, int]],
) -> Tuple[int, List[str]]:
    """Resuelve la compra de fruta mediante mochila 0/1 y backtracking.

    Parámetros:
        budget: presupuesto máximo disponible, en euros enteros.
        items: lista de tuplas
               (name, price_per_kg, units_per_kg).
               Cada tupla representa un pack indivisible de 1 kg disponible
               una sola vez.

    Debe devolver:
        (best_units, best_set)

    donde best_units es el máximo número total aproximado de piezas de fruta y
    best_set es la lista de nombres de los packs elegidos, ordenada
    lexicográficamente.

    Criterios de desempate:
        1. Mayor número total de piezas.
        2. A igualdad, menor coste total.
        3. A igualdad, lista de nombres lexicográficamente menor.

    Estrategia obligatoria:
        - Backtracking recursivo.
        - Para cada pack: incluirlo o excluirlo.
        - Poda por presupuesto.
        - Cada pack puede elegirse como máximo una vez.

    No debes leer datos ni imprimir mensajes en esta función.
    """

    def peso(solution):
        peso = 0
        for i, item in enumerate(solution):
            if item == 1:
                peso += items[i][1]
        return peso

    def valor(solution):
        valor = 0
        for i, item in enumerate(solution):
            if item == 1:
                valor += items[i][2]
        return valor

    def nombres(solution):
        nombres = []
        for i, item in enumerate(solution):
            if item == 1:
                nombres.append(items[i][0])
        return sorted(nombres)

    def is_valid_solution(solution):
        if peso(solution) > budget: 
            return False
        else: 
            return True

    def dfs(solution, level):
        nonlocal best_solution
        
        if is_valid_solution(solution) is False:
            return

        if (valor(solution) > valor(best_solution)):
            best_solution = solution.copy()
        elif (valor(solution) == valor(best_solution)) and (peso(solution) < peso(best_solution)):
            best_solution = solution.copy()
        elif (valor(solution) == valor(best_solution)) and (peso(solution) == peso(best_solution)) and (nombres(solution) < nombres(best_solution)):
            best_solution = solution.copy()


        if level == len(solution): return

        for i in range(2):
            new_solution = solution.copy()
            new_solution[level] += i
            dfs(new_solution, level + 1)
        
        pass

    best_solution = [0] * len(items)
    solution = [0] * len(items)

    dfs(solution, 0)


    best_set = nombres(best_solution)

    final = (valor(best_solution), sorted(best_set))



    return final
