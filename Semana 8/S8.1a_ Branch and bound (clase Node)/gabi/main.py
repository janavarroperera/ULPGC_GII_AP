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

first_line = get_line(input_source).split()
item_count = int(first_line[0])
capacity = int(first_line[1])
    
items = []
for i in range(1, item_count+1):
    parts = get_line(input_source).split()
    items.append(Item(i-1, int(parts[0]), int(parts[1])))
    
node1 = Node(1, [], 0, capacity)
node2 = Node(2, [1], items[1].value, capacity - items[1].weight)
node3 = Node(3, [2], items[2].value, capacity - items[2].weight)

print("Node 1: " + str(node1.index) + " " + str(node1.room) + " " + str(node1.taken) + " " + str(node1.value) + " " + str(node1.estimate(items)))
print("Node 2: " + str(node2.index) + " " + str(node2.room) + " " + str(node2.taken) + " " + str(node2.value) + " " + str(node2.estimate(items)))
print("Node 3: " + str(node3.index) + " " + str(node3.room) + " " + str(node3.taken) + " " + str(node3.value) + " " + str(node3.estimate(items)))

# ----------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)
