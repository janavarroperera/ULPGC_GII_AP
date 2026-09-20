
def solve(input_list):
    """
    Calcula la suma de los valores de calibración de una lista de cadenas.

    Parámetros:
        input_list: lista de cadenas de texto. Cada cadena puede contener letras,
        dígitos u otros caracteres.

    Funcionamiento esperado:
        1. Procesar cada cadena de input_list.
        2. Localizar el primer dígito y el último dígito de cada cadena.
        3. Formar un número de dos cifras con esos dos dígitos.
        4. Si una cadena contiene un solo dígito, usarlo como primera y última cifra.
        5. Si una cadena no contiene dígitos, no sumar nada por esa cadena.
        6. Devolver la suma total de todos los números obtenidos.

    Restricciones:
        - No leer datos por teclado dentro de esta función.
        - No imprimir resultados dentro de esta función.
        - Devolver un número entero.
    """
    result = 0
    for string in input_list:
        first = ""
        last = ""
        for char in string:
            if char.isdigit() and first == "":
                first = char
            elif char.isdigit():
                last = char
        if last == "":
            last = first
        result += int(first+last)

    return result

