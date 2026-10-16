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

    solution = [0] * len(items)
    best_solution = [0] * len(items)

    def cost(solution):
        total = 0
        for i, item in enumerate(solution):
            if item == 1:
                total += items[i][1]
        return total

    def value(solution):
        total = 0
        for i, item in enumerate(solution):
            if item == 1:
                total += items[i][2]
        return total

    def names(solution):
        name_list = []
        for i, item in enumerate(solution):
            if item == 1:
                name_list.append(items[i][0])
        return sorted(name_list)

    def is_valid(solution):
        if cost(solution) > budget:
            return False
        else:
            return True

    def backpack(solution, level):
        nonlocal best_solution
        if is_valid(solution) == False:
            return

        if (value(solution) > value(best_solution)):
            best_solution = solution.copy()
        elif (value(solution) == value(best_solution)) and (cost(solution) < cost(best_solution)):
            best_solution = solution.copy()
        elif (value(solution) == value(best_solution)) and (cost(solution) < cost(best_solution)) and (names(solution) < names(best_solution)):
            best_solution = solution.copy()

        if level == len(solution):
            return


        for i in range(2):
            solution_copy = solution.copy()
            solution_copy[level] += i
            backpack(solution_copy, level+1)

    backpack(solution, 0)

    return (value(best_solution), names(best_solution))
    
    
