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

    numeros_dic = {
        "zero":0,
        "one": 1,
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
    clean_list = []
    number_list = []

    for item in input_list:
        if item[-1] == '\r':
            clean_list.append(item[0:-1])
        else:
            clean_list.append(item)

    for item in clean_list:
        numbers = re.findall(r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))", item)
        first = numbers[0]
        last = numbers[-1]

        try:
            first = int(first)
        except ValueError:
            first = numeros_dic[first]

        try:
            last = int(last)
        except ValueError:
            last = numeros_dic[last]

        number_list.append(first*10 + last)
    
    for number in number_list:
        counter += number

    return counter