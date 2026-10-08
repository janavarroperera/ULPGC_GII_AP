
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
