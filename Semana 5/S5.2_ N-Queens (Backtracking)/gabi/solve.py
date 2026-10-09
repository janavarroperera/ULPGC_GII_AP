def solve(num_queens):
   """
   Using backtracking compute all the solutions to place the
   given number of queens in a square board  
   :param num_queens: number of queens to place in the board
   :return: list of lists containing all the solution 
   For example, if num_queens = 4 there are two solutions,
   and it returns:
      solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1]   
   """
   
   solutions_list = []
   # solve it here!
   def is_valid_solution(solution, level):
        placed = solution[:level]

        if len(set(placed)) != len(placed):
            return False

        # Check for diagonals
        coordinates = []
        for idx, queen in enumerate(placed):
            j = queen
            i = idx
            coordinates.append((i, j))

        for i, coordinate in enumerate(coordinates):
            i += 1
            while i < len(coordinates):
                if abs(coordinates[i][0] - coordinate[0]) == abs(coordinates[i][1] - coordinate[1]):
                    return False
                i += 1
        return True


   solution = [-1] * num_queens

   def dfs(level):
       # Si la solución que tengo construida hasta este nivel
       # no es válida subimos al nivel anterior ('backtrack’)
       if not is_valid_solution(solution, level):
           return
       # Si tengo todos los digitos de una solución, la proceso
       # y continúo el recorrido DFS.
       elif level == num_queens:
           solutions_list.append(solution.copy())
           return
       else:
           # Continúo con el recorrido en profundidad
           for digit in range(0, num_queens):
               solution[level] = digit
               dfs(level+1)
               solution[level] = -1
           return

   dfs(0)

   
   return solutions_list
