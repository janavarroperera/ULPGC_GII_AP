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
from solve import *

# Dígitos: número de posiciones y dominio de cada una
num_digits = int(get_line(input_source).split()[0])
digit_values = []
for line in get_n_lines(input_source, num_digits):
    digit_values.append([int(value) for value in line.split()])

# Letras: número de posiciones y dominio de cada una
num_letters = int(get_line(input_source).split()[0])
letter_values = []
for line in get_n_lines(input_source, num_letters):
    letter_values.append(line.split())

plates = Plate_Iterator(num_digits, digit_values, num_letters, letter_values)

for plate in plates.next():
    print(plate)

# ----------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)
