#!/usr/bin/env python3
from utils import open_test_file, close_test_file, get_line
from solve import solve_mfd_feasible

# test_file = "test1.txt"
test_file = "test.txt"
input_source = open_test_file(test_file)

first = get_line(input_source).strip()
n_str, m_str = first.split()
n, m = int(n_str), int(m_str)
exams_line = get_line(input_source).strip()
rooms_line = get_line(input_source).strip()

exams = list(map(int, exams_line.split()))
rooms = list(map(int, rooms_line.split()))

res = solve_mfd_feasible(exams, rooms)

result = "ERROR"
if res is not None:
    rooms_used, waste, assign_cap = res
    result = f"rooms_used={rooms_used} waste={waste}\nassign={assign_cap}"

print(result)

close_test_file(test_file, input_source)
