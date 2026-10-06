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


first_line = get_line(input_source).split()
num_digits = int(first_line[0])
base       = int(first_line[1])


# Usando la implementacion con generador (yield)
from solve_yield import My_Iterator
obj = My_Iterator(num_digits, base)
for c in obj.next():
    print(c)


# Usando la implementacion con iterador
# from solve_iter import My_Iterator
# obj = My_Iterator(num_digits, base)
# for c in obj:
#     print(c)

# ----------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)
