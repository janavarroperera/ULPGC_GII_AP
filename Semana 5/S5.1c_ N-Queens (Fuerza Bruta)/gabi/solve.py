from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    # solve it here!    
    iterator = My_Iterator(num_queens, num_queens)
    for candidate in iterator.next():
        valid = True
        set_candidate = set(candidate)
        if len(set_candidate) != num_queens:
            # Remove those in the same row
            continue

        # Check for diagonals
        coordinates = []
        for idx, queen in enumerate(candidate):
            j = queen
            i = idx
            coordinates.append((i, j))

        for i, coordinate in enumerate(coordinates):
            i += 1
            while i < len(coordinates):
                if abs(coordinates[i][0] - coordinate[0]) == abs(coordinates[i][1] - coordinate[1]):
                    valid = False
                    break
                i += 1
            
            
        if valid:
            solutions_list.append(list(candidate))
            
                
                


    return solutions_list
