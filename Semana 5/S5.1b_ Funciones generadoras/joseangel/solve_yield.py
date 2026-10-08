# 1. Copia aqui tu solución del primer ejercicio de esta semana

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
# ----------------------------------------------------------

# main.py recorre el objeto My_Iterator e imprime cada lista obtenida.
class My_Iterator:

    def __init__(self, num_digits, base):
        # Guarda la longitud de cada lista y la base para la iteración.
        self.num_digits = num_digits # longitud de cada lista
        self.base = base
        self.actual = [0] * num_digits
        pass

    def is_last_value(self, digits):
        # Indica si todos los dígitos han alcanzado el último valor posible.
        for digit in digits:
            if digit != self.base - 1:
                return False
        return True
           
            

    def next(self):
        # Devuelve la combinación actual y prepara la siguiente con next_number.
        while self.is_last_value(self.actual) == False:
            yield self.actual
            self.actual = next_number(self.actual, self.base)
        yield self.actual
