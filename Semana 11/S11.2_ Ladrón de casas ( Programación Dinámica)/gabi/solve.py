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
        i = len(table) -1
        while i >= 0:
            a = table[i-1] if i >= 1 else 0
            if table[i] == a:
                i -= 1
            else:
                taken.append(i+1)
                i -= 2

        taken.reverse()
        return
        
    fill_table()
    fill_taken()
    return table[taken[-1]-1], taken
    


def solve_memoization(items):
    taken = []
    mem = {}


    def t(n):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        # ...
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        if (n in mem):
            return mem[n]
        else:
            mem[n] = max((t(n-2) + items[n]), t(n-1))
            return mem[n]

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        return

    n = len(items) - 1   

    if n == 0:
        return items[n], 0
    elif n == 1:
        return max(items[n], items[n-1]), 0
    
    mem[0] = items[0]
    mem[1] = max(items[0], items[1])
     
    
    max_benefit = t(n)
    print(max_benefit)

    fill_taken()
    
    return 0, taken

