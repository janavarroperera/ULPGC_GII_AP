import sys


def open_test_file(test_file):
    if test_file is not None:
        input_source = open(test_file, "r", newline="")
    else:
        input_source = sys.stdin
    return input_source


def close_test_file(test_file, input_source):
    if test_file is not None:
        input_source.close()
    return


def get_line(input_source):
    return input_source.readline().rstrip("\n")


def get_n_lines(input_source, n):
    input_list = []
    for j in range(n):
        input_list.append(get_line(input_source))
    return input_list
