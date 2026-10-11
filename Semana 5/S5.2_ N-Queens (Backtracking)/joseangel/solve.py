
def solve(num_queens):
   """
   :param num_queens: number of queens to place in the board
   :return: list of lists containing all the solutions
   """
   solution = [-1] * num_queens
   solutions_list = []



   def is_valid_solution(posible_solution):
      """
      funcion que dada una posible_solution devuelve True si esa solucion es valida
      """
      for queen in posible_solution:
         if queen == -1:
               break
         if posible_solution.count(queen) >= 2:
               return False

      j = 0
      while (j < num_queens - 1):
         i = 1
         while (i < num_queens - j):
            if (posible_solution[j + i] == posible_solution[j] + i) or ((posible_solution[j + i] == posible_solution[j] - i) and (posible_solution[j + i] >= 0)):
               return False
            i += 1
         j += 1

      return True

   def dfs(solution, level):

      if is_valid_solution(solution) is False: 
         return

      if -1 in solution:
         for i in range(1, num_queens + 1):
            next_solution = solution.copy()
            next_solution[level] += i
            dfs(next_solution, level + 1)
         return

      solutions_list.append(solution)
      return


   # solve it here!
   dfs(solution, 0)
   

   return solutions_list
