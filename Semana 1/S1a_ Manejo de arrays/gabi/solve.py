
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

    bottom = int(input_list[2][0])
    top = int(input_list[3])

    padre:str = input_list[0][0:-1]

    padre = padre.split(",")

    padre_lista = []
    for numero in padre:
        padre_lista.append(int(numero))


    madre:str = input_list[1][0:-1]

    madre = madre.split(",")

    madre_lista = []
    for numero in madre:
        madre_lista.append(int(numero))

    print(padre_lista)
    print(madre_lista)

    hijo = [None] * len(padre_lista)
    print(hijo)
    print(top)
    print(bottom)

    current = bottom
    while current < top:
        hijo[current] = padre_lista[current]
        current += 1
    print(hijo)

    i = top
    j = top
    while None in hijo:
        if hijo[i] == None:
            

    print(hijo)
