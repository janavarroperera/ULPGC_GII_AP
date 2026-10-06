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
    # ...

    carry = 0

    if next_digits[-1] == (base - 1):
        carry = 1
        next_digits[-1] = 0
    else:
        next_digits[-1] = next_digits[-1] + 1
    
    i = len(next_digits) - 2
    while i >= 0:
        if carry == 1 and next_digits[i] == (base - 1):
            next_digits[i] = 0
        elif carry == 1 and next_digits[i] == 0:
            next_digits[i] = next_digits[-1] + 1
            carry = 0
        i -= 1

    return next_digits

def next_number(digits, base):
    # Devuelve una lista nueva con el siguiente número en la base indicada.
    pass

# ----------------------------------------------------------

# main.py recorre el objeto My_Iterator e imprime cada lista obtenida.
class My_Iterator:

    def __init__(self, num_digits, base):
        # Guarda la longitud de cada lista y la base para la iteración.
        pass

    def __is_last_value__(self, digits):
        # Indica si todos los dígitos han alcanzado el último valor posible.
        pass

    def __iter__(self):
        # Inicializa la iteración desde la lista de ceros y devuelve self.
        pass

    def __next__(self):
        # Devuelve la combinación actual y prepara la siguiente con next_number.
        # Tras devolver la última, termina con StopIteration en la siguiente llamada.
        pass
