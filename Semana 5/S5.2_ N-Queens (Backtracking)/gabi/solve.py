
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
           ...
           return
       else:
           # Continúo con el recorrido en profundidad
           for digit in solution:
               solution[level] = digit
               dfs(level+1)
           solution[level] = -1
           return

   dfs(0)
   
   return solutions_list
