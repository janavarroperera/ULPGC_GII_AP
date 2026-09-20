from utils import open_test_file, close_test_file, get_line, get_n_lines
from solve import solve

TEST_FILE = "test.txt"

input_source = open_test_file(TEST_FILE)

first_line = get_line(input_source).split()
num_lines = int(first_line[0])
input_list = get_n_lines(input_source, num_lines)

solution = solve(input_list)

print(solution)

close_test_file(TEST_FILE, input_source)
