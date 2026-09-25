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
    items_clean = []
    for item in items:
        move = (item.strip()[0], int(item.strip()[1:]))
        items_clean.append(move)

    pos = [0, 0]
    looking = 0
    for move in items_clean:
        if move[0] == 'R':
            looking = (looking + 1) % 4
        else:
            looking = (looking - 1) % 4

        if looking == 0:
            pos[1] += move[1]
        elif looking == 1:
            pos[0] += move[1]
        elif looking == 2:
            pos[1] -= move[1]
        elif looking == 3:
            pos[0] -= move[1]
    
    return abs(pos[0]) + abs(pos[1])
