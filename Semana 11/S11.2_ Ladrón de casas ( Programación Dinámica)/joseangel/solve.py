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
        i = n
        while i >= 0:
            sin = t(i - 1) if i >= 1 else 0
            if t(i) == sin:
                i -= 1
            else:
                taken.append(i + 1)
                i -= 2
        taken.reverse()

    
    max_benefit = t(n)
    fill_taken()
    
    return max_benefit, taken

