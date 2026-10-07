
def next_number(digits, base):
    """
    :param digits: list containing all the digits of a number 
                   in the given base
    :param base: numeric base of the number
    :return: list representing the next value of the number

     Example: digits = [0, 1, 0, 1]   number 5
                base = 2

              returns [0, 1, 1, 0]    number 6
    """

    next_digits = digits.copy()

    # Añade tu código aqui
    i = -1
    while True:
      try:
        next_digits[i] += 1
      except IndexError:
        return next_digits
      
      if next_digits[i] >= base:
        next_digits[i] = 0
        i -= 1
      else: 
        return next_digits
