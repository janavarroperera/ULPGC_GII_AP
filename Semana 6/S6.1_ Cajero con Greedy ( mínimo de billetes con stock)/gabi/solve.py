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

    if total <= 0 or total % 10 != 0:
        return None
    
    

    def sum_bills(bills):
        return (bills[0] * 10) + (bills[1] * 20) + (bills[2] * 50)

    final_bills = [0, 0, 0]

    def greedy(bills:list) -> bool:
        nonlocal final_bills
        if sum_bills(bills) == total:
            final_bills = bills
            return True

        if sum_bills(bills) + 50 <= total and bills[2] +1 <= max50:
            bills_copy = bills.copy()
            bills_copy[2] += 1
            if greedy(bills_copy):
                return True

        if sum_bills(bills) + 20 <= total and bills[1] +1 <= max20:
            bills_copy = bills.copy()
            bills_copy[1] += 1
            if greedy(bills_copy):
                return True

        if sum_bills(bills) + 10 <= total and bills[0] +1 <= max10:
            bills_copy = bills.copy()
            bills_copy[0] += 1
            if greedy(bills_copy):
                return True

        return False



    greedy([0, 0, 0])    # 10, 20, 50

    if sum_bills(final_bills) != total:
        return None
    else:
        return final_bills
