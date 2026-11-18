# -----------------------------------------------------------------
# Para redireccionar la entrada en Wing 101 crea un fichero con
# los datos de entrada en la misma carpeta donde tienes el fichero
# main.py de este ejercicio y añade aquí una string con el nombre
# del fichero.
#    Ejemplo:
#    test_file = "test1.txt"

from utils import *

test_file    = None
input_source = open_test_file (test_file)

# ----------------------------------------------------------------
from collections       import namedtuple
from solve import *

Item = namedtuple("Item", ['index', 'value', 'weight'])

first_line = get_line(input_source).split() 	# N, Capacity
N          = int(first_line[0])
capacity   = int(first_line[1])

items = []
for i in range(1, N+1):
    parts = get_line(input_source).split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

# Comenzamos programando la recurrencia mediante tabulation
value1, taken1 = solve_tabulation(items, capacity)


print(value1, taken1)

# Cuando termines tabulation, comenta el código anterior
# para desactivarlo (la llamada a solve_tabulation y los
# dos print) y descomenta las siguientes lineas para que
# programes la recurrencia mediante memoization.

# value2, taken2 = solve_memoization(items, capacity)
# print(value2, taken2)

# Cuando termines los dos ejercicios puedes activar estas
# lineas para comprobar que los dos dan exactamente los
# mismos resultados.

# assert value1 == value2
# assert taken1 == taken2

# ----------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)
