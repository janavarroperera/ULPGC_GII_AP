# License Plate Iterator (My_Iterator / Plate_Iterator)

## Contexto

A car license plate consists of 4 digits followed by 3 letters (for example, `1234BCD`). If we want to enumerate all the possible combinations (license plates) from specific domains for each position, we can view the problem as the Cartesian product of two independent parts: the numeric part (4 positions) and the alphanumeric part (3 positions).

The idea of this exercise is to combine two iterators based on `yield`: one generates all the combinations of digits and the other all the combinations of letters. A combined iterator traverses the first one and, for each combination of digits, exhausts the second one (every combination of letters), emitting the complete license plate.

## Objetivo

Program the required algorithm using `yield`:

1. A generic iterator `My_Iterator` that generates all possible combinations of `num_positions` positions, where each position takes values from a specific domain.
2. A combined iterator `Plate_Iterator` that uses two `My_Iterator` (one for the 4 digits and another for the 3 letters) and generates each license plate as a string with the format `"NNNNLLL"`.

> **NOTE:** Each combination is produced as a list, in the same order that any nested loop would produce it: the numeric part varies slowest and, for each numeric combination, the letter part varies fastest (the last letter is the first to change).

## Formato de entrada

```
num_digits
d1_1 d1_2 ... d1_k
d2_1 d2_2 ... d2_m
d3_1 d3_2 ... d3_p
d4_1 d4_2 ... d4_q
num_letters
l1_1 l1_2 ... l1_r
l2_1 l2_2 ... l2_s
l3_1 l3_2 ... l3_t
```

where:

- **Line 1:** an integer `num_digits` with the number of numeric positions (4 for a license plate).
- **Next `num_digits` lines:** the domain values of each digit, separated by spaces (integers).
- **Next line:** an integer `num_letters` with the number of letter positions (3 for a license plate).
- **Next `num_letters` lines:** the domain values of each letter, separated by spaces (one-character strings).

## Formato de salida

Each license plate is printed on its own line, as a string made up of the 4 digits followed by the 3 letters:

```
NNNNLLL
```

## Ejemplo de caso de prueba

**Input:**

```
4
1 2
3 4
5 6
7 8
3
A B
C D
E F
```

**Expected output (first lines):**

```
1357ACE
1357ACF
1357ADE
1357ADF
...
2468BDF
```

In total, 2\*2\*2\*2 \* 2\*2\*2 = 128 license plates are generated.

## Tarea del alumno

Implement the classes `My_Iterator` and `Plate_Iterator` in the file `solve.py`:

```python
class My_Iterator:
    def __init__(self, num_positions, value_lists):
        """Stores the iterator configuration."""

    def next(self):
        """Generator that produces each combination as a list using yield."""


class Plate_Iterator:
    def __init__(self, num_digits, digit_values, num_letters, letter_values):
        """Builds two My_Iterator objects: one for digits and one for letters."""

    def next(self):
        """Combines both iterators with yield and produces each license plate
        as a string 'NNNNLLL'."""
```

The classes to implement must:

- Use `yield` to generate the combinations / license plates.
- `My_Iterator` must produce the combinations in nested-loop order (last position varies fastest).
- `Plate_Iterator` must combine the two iterators: for each combination of digits, traverse all combinations of letters.
- Not use external libraries (`itertools`) or `yield from`.

> **NOTE:** Using `yield from` or `itertools` is not allowed.

**Main files:**

- `main.py`: reads the input, builds the combined iterator and uses it to print the license plates.
- `solve.py`: contains the classes `My_Iterator` and `Plate_Iterator` that the exercise asks you to implement.
