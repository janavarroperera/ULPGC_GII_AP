
import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1,capacity+1), dtype=int)

    def fill_table():
        return

    def fill_taken():
        return

    fill_table()
    fill_taken()
    return 0, taken



def solve_memoization(items, capacity):
    taken = []
    mem={}

    def t(n,w):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        # ...
        return 0

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de los items elegidos.
        # ...

        return

    n = len(items)-1

    max_benefit = t(n,capacity)
    fill_taken()

    return 0, taken
    