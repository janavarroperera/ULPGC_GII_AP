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

    solution = [0, []]

    def backpack(solution, level):
        ...

    

    
