
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
