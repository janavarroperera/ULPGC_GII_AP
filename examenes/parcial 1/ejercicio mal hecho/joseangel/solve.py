# Reglas: usa `yield` en los generadores.
# NO se permite `yield from` ni `itertools`.

def next_combination(combination, value_lists):
    new_combination = combination.copy()
    i = -1
    
    while True:
        try:
            new_combination[i]
        except IndexError:
            return new_combination

        j = value_list.index(new_combination[i])

        if j + 1 == len(value_list):
            j = 0
            new_combination[i] = value_list[j]
            i -= 1
            continue

        new_combination[i] = value_lists[i][j + 1]
        print(new_combination)
        return new_combination



class My_Iterator:

    def __init__(self, num_positions, value_lists):
        """Stores the iterator configuration."""
        self.num_positions = num_positions
        self.value_list = value_lists
        self.combination = [None] * self.num_positions


    def next(self):
        """Generator that produces each combination as a list using yield."""
        if None in self.combination:
            self.combination = [self.value_list[0]] * self.num_positions

        while self.is_last_value(self.combination) is False: 
            yield self.combination 
            self.combination = next_combination(self.combination, self.value_list)
        yield self.combination
        
    def is_last_value(self, combination):
        last = [self.value_list[-1]] * self.num_positions
        if last == combination:
            return True
        else:
            return False

    def __str__(self):
        return self.num_positions, self.value_list

class Plate_Iterator:

    def __init__(self, num_digits, digit_values, num_letters, letter_values):
        """Builds two My_Iterator objects: one for digits and one for letters."""
        # Añade tu código aqui

    def next(self):
        """Combines both iterators with yield and produces each license plate
        as a string 'NNNNLLL'."""
        return [0]
