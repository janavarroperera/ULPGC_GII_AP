# Reglas: usa `yield` en los generadores.
# NO se permite `yield from` ni `itertools`.

def next_number(digits):
    


class My_Iterator:

    def __init__(self, num_positions, value_lists):
        """Stores the iterator configuration."""
        # Añade tu código aqui
        self.num_positions = num_positions
        self.value_lists = value_lists

    def next(self):
        """Generator that produces each combination as a list using yield."""
        # Añade tu código aqui




class Plate_Iterator:

    def __init__(self, num_digits, digit_values, num_letters, letter_values):
        """Builds two My_Iterator objects: one for digits and one for letters."""
        # Añade tu código aqui
        self.num_digits = num_digits
        self.digit_values = digit_values
        self.num_letters = num_letters
        self.letter_values = letter_values

    def next(self):
        """Combines both iterators with yield and produces each license plate
        as a string 'NNNNLLL'."""
        # Añade tu código aqui
