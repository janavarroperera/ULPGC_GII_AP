# solve_vpl.py — Esqueleto para alumnos

def solve(total: int, max10: int, max20: int, max50: int) -> tuple[int, int, int] | None:
    """
    Calcula una combinación de billetes de 10, 20 y 50 que suma exactamente
    el importe `total`, respetando el stock disponible para cada denominación
    (`max10`, `max20`, `max50`) y minimizando el número total de billetes.

    Estrategia Greedy:
    - Si `total` es negativo o no es múltiplo de 10, devuelve None.
    - Intenta primero con el mayor número posible de billetes de 50
      (sin superar `max50`) y, para cada cantidad de 50 fijada:
        1) Calcula el resto y toma el máximo posible de billetes de 20 (≤ `max20`).
        2) Ajusta los billetes de 20 hacia abajo hasta que el resto sea múltiplo de 10.
        3) Completa el resto con billetes de 10 y verifica que no supere `max10`.
        4) Si la combinación respeta el stock, devuelve la tupla (B10, B20, B50).
    - Si no existe combinación válida, devuelve None.
    """

    return None
