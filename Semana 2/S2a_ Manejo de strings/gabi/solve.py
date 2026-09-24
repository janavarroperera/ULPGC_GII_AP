import re
def solve(input_list):
    """
    Calcula la suma de los valores de calibración de una lista de líneas.

    Cada línea puede contener dígitos numéricos y/o dígitos escritos en inglés:
    zero, one, two, three, four, five, six, seven, eight, nine.

    Para cada línea se debe formar un número de dos cifras con:
        - el primer dígito que aparece al recorrer la línea de izquierda a derecha;
        - el último dígito que aparece al recorrer la línea de izquierda a derecha.

    Las palabras pueden solaparse. Por ejemplo:
        - "twone" contiene "two" y "one", por tanto produce 21.
        - "oneight" contiene "one" y "eight", por tanto produce 18.

    Parámetros:
        input_list: lista de cadenas de texto, una por cada línea de entrada.

    Restricciones:
        - No leer datos por teclado dentro de esta función.
        - No imprimir resultados dentro de esta función.
        - Devolver un entero con la suma total.
    """
    print(input_list)
    num_dict = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }

    counter = 0
    number_list = []

    for string in input_list:
        first = 0
        last = 0

        numbers = re.findall(r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))", string)

        try:
            first = int(numbers[0])
        except ValueError:
            first = num_dict[numbers[0]]

        try:
            last = int(numbers[-1])
        except ValueError:
            last = num_dict[numbers[-1]]

        number_list = [first*10 + last]

        for number in number_list:
            counter += number

    return counter
