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
   obj = My_Iterator(num_queens, num_queens)
   for solution in obj:
      evaluando_solucion = solution.copy()
      evaluando_solucion = set(evaluando_solucion)
      if len(evaluando_solucion) != num_queens:
         continue

      # if solution == [0, 2, 4, 1, 3]:
      #    print(1)
      
      j = 0
      is_valid = True
      while j < num_queens-1:
         i = 1
         while i < num_queens - j:
            if solution[j + i] == solution[j] + i or solution[j + i] == solution[j] - i:
               i += 1
               is_valid = False
            else:
               i += 1

         j += 1

      if is_valid is True:
         solutions_list.append(solution)
   
      
      
      
   


   return solutions_list