# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = []
    taken = []
    
    def fill_table():
        # Primera fase: Rellenamos la lista 'table' con las
        # soluciones de todos los subproblemas (o sea, los
        # beneficios que puede conseguir el ladrón).
        # ...
        for i, house in enumerate(items):
            if (i < 2):
                table.append(house)
                continue
            table.append(max((table[i-2] + items[i]), table[i-1]))
        return
        
    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        taken.append(0)
        last_value = -1
        taken_index = 0
        for i, value in enumerate(table):
            if last_value == value:
                taken_index += 1
                taken.append(0)
            last_value = value
            taken[taken_index] = i+1

        return
        
    fill_table()
    fill_taken()
    return table[taken[-1]-1], taken
    


def solve_memoization(items):
    mem = {}
    taken = []

    def t(n):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        # ...
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        return 0

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        return

    n = len(items) - 1    
    
    max_benefit = t(n)
    fill_taken()
    
    return 0, taken

