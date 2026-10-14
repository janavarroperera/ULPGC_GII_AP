from utils import open_test_file, close_test_file, get_line
from solve import solve


# Ejemplo: "test1.txt" para pruebas locales
TEST_FILE = None
# TEST_FILE = "test1.txt"

def read_nonempty_line(source):
    line = get_line(source)
    while line is not None and line.strip() == "":
        line = get_line(source)
    return line


inp = open_test_file(TEST_FILE)

first_line = read_nonempty_line(inp)
num_items, budget = map(int, first_line.split())
items = []

for _ in range(num_items):
    line = read_nonempty_line(inp)
    name, price_text, units_text = line.split()
    price_per_kg = int(price_text)
    units_per_kg = int(units_text)
    items.append((name, price_per_kg, units_per_kg))

best_units, best_set = solve(budget, items)
print(f"{best_units} {best_set}")

close_test_file(TEST_FILE, inp)
