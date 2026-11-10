# -----------------------------------------------------------------
# Para redireccionar la entrada en Wing 101 crea un fichero con
# los datos de entrada en la misma carpeta donde tienes el fichero
# main.py de este ejercicio y añade aquí una string con el nombre
# del fichero.
#    Ejemplo:
#    test_file = "test1.txt"

from utils import *

test_file    = "test.txt"
input_source = open_test_file (test_file)

# ----------------------------------------------------------------
from collections import namedtuple

from node import *
from solve import *

first_line = get_line(input_source).split()
item_count = int(first_line[0])
capacity = int(first_line[1])
    
items = []
for i in range(1, item_count+1):
    parts = get_line(input_source).split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

value, taken, visiting_order = solve_branch_and_bound_DFS(capacity, items, True)

print(visiting_order)
print(value)
print(taken)

# ----------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)
