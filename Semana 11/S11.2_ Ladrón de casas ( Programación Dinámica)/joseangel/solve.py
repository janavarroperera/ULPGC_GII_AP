# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = [0] * len(items) 
    taken = []
    
    def fill_table():
        for i, valor in enumerate(table):
            if i == 0: #casos base
                table[i] = items[i]
            elif i == 1:
                table[i] = max(items[i], items[i-1])
            else:
                table[i] = max(table[i-2] + items[i], table[i-1])
        return
        
    def fill_taken():
        i = len(table) - 1
        while i >= 0:
            if table[i] > table[i-1]:
                taken.append(i)
                i -= 2
            elif table[i] == table[i-1]:
                i -= 1
            else:
                taken.append(i)
        sorted(taken)
        return
    
        
    fill_table()
    fill_taken()
    return table[-1], taken
    


def solve_memoization(items):

    n = len(items) - 1    
    if n == 0:
        return items[0]
    if n == 1:
        return max(items[0], items[1])
    
    mem = {0: items[0],
           1: max(items[0], items[1])}
    taken = []

    def t(i):
        if i in mem:
            return mem[i]
        else:
            mem[i] = max(items[i] + t(i -2), t(i - 1))
            return mem[i]
            

        return 0

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        return

    
    max_benefit = t(n)
    fill_taken()
    
    return max_benefit, taken

