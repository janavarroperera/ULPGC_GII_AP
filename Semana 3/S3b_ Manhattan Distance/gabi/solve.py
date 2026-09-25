def solve(items):
    """Calcula la distancia de Manhattan tras ejecutar las instrucciones.

    Parámetros:
        items: lista no vacía de cadenas con instrucciones como 'R2' o 'L3'.
            Cada instrucción indica un giro de 90 grados a la izquierda (L)
            o a la derecha (R), seguido del número de cuadrículas que avanzar.
            La lista no incluye el número de instrucciones de la entrada.

    Se parte de la posición (0, 0), mirando hacia el Norte. Las instrucciones
    se ejecutan en orden, girando primero y avanzando después.

    Devuelve:
        Un entero con la distancia de Manhattan entre la posición inicial
        y la final, no la longitud total del recorrido.

    Ejemplos:
        solve(['R2', 'L3']) debe devolver 5.
        solve(['R3', 'R3', 'R2']) debe devolver 4.
        solve(['R5', 'L5', 'R5', 'R3']) debe devolver 12.

    No debe leer datos ni imprimir: main.py gestiona la entrada y la salida.
    """
    print(items)

    position = [0, 0]

    # If looking north, y++, south y--, east x++, west x--
    heading = "N"

    for command in items:
        command = command.strip()
        # check and do the turn:
        if command[0] == "R":
            if heading == "N":
                heading = "E"
            elif heading == "E":
                heading = "S"
            elif heading == "S":
                heading = "W"
            else:
                heading = "N"
        else:
            if heading == "N":
                heading = "W"
            elif heading == "W":
                heading = "S"
            elif heading == "S":
                heading = "E"
            else:
                heading = "N"

        # Move verticaly
        if heading == "N":
            position[1] += int(command[1:])
        elif heading == "S":
            position[1] -= int(command[1:])
        elif heading == "E":
            position[0] += int(command[1:])
        else:
            position[0] -= int(command[1:])

    return abs(position[0]) + abs(position[1])

