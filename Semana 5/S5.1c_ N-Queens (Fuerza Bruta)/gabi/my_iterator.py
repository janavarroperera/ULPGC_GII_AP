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

    next_digits = []

    # Añade tu código aqui
    # ...

    carry = 0

    is_first = True

    for digit in reversed(digits):
        if is_first:
            if digit < base -1:
                next_digits.append(digit+1)
            else:
                carry = 1
                next_digits.append(0)
            is_first = False
        else:
            if carry == 1:
                if digit + carry > base -1:
                    next_digits.append(0)
                else:
                    next_digits.append(digit+carry)
                    carry = 0
            else:
                next_digits.append(digit)
                
    next_digits.reverse()
    return next_digits



# ----------------------------------------------------------

# main.py recorre el objeto My_Iterator e imprime cada lista obtenida.
class My_Iterator:

    def __init__(self, num_digits, base):
        # Guarda la longitud de cada lista y la base para la iteración.
        self.num_digits = num_digits
        self.base = base
        self.current_digits = [0] * self.num_digits

    def is_last_value(self, digits):
        # Indica si todos los dígitos han alcanzado el último valor posible.
        for digit in digits:
            if digit != (self.base -1):
                return False
        return True

    def next(self):
        # Devuelve la combinación actual y prepara la siguiente con next_number.
        while self.is_last_value(self.current_digits) == False:
            self.current_digits = next_number(self.current_digits, self.base)
            yield self.current_digits