
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

    def limpiar_lista(lista_a_limpiar):
        lista_final = []

        lista_a_limpiar = lista_a_limpiar.split(",")

        for numero in lista_a_limpiar:
            lista_final.append(int(numero))

        return lista_final


    padre = input_list[0][0:-1]
    madre = input_list[1][0:-1]

    padre = limpiar_lista(padre)
    madre = limpiar_lista(madre)

    lower_bound = int(input_list[2][0:-1])
    upper_bound = int(input_list[3])

    hijo = [None] * len(padre)
    hijo[lower_bound:upper_bound] = padre[lower_bound:upper_bound] 

    i = upper_bound % len(hijo)
    j = upper_bound % len(madre)
    while None in hijo:
        if hijo[i] is None:
            if madre[j] not in hijo:
                hijo[i] = madre[j]
                if i == len(hijo) - 1:
                    i = 0
                else:
                    i += 1

            if j == len(madre) -1:
                j = 0
            else:
                j += 1


        else: 
            if i == len(hijo) - 1:
                i = 0
            else:
                i += 1

    return hijo

