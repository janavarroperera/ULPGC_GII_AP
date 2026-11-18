from utils import open_test_file, close_test_file, get_line
from solve import solve_project_teams

TEST_FILE = None  # Cambia a 'test1.txt' para depurar

inp = open_test_file(TEST_FILE)
first = get_line(inp)
if not first:
    raise SystemExit(0)
n, k = map(int, first.strip().split())

teams, table = solve_project_teams(n, k)

print(f"Teams={teams}")
print("DP_Table:")
for i, row in enumerate(table):
    print("row {}: {}".format(i, " ".join(map(str, row))))

close_test_file(TEST_FILE, inp)
