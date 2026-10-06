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
from solve import *

first_line = get_line(input_source).split()
num_values = int(first_line[0])
base       = int(first_line[1])

for j in range(num_values):
    data = get_line(input_source)

    # Convertimos la string en la lista que contiene
    # el número de entrada.
    digits = []
    for digit in data:
        digits.append(int(digit))

    # Mostramos la lista con el número de entrada y
    # la lista con el siguiente número.
    print(digits, '- ', end="")
    print(next_number(digits, base))

# ----------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)
