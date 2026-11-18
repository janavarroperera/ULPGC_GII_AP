# Construir la tabla DP de coeficientes binomiales.

from typing import List, Tuple

"""
Ejemplo: build_pascal_table_k(4, 2)

[
  [1],        # i=0 -> C(0,0)
  [1, 1],     # i=1 -> C(1,0..1)
  [1, 2, 1],  # i=2
  [1, 3, 3],  # i=3, truncado a k=2
  [1, 4, 6],  # i=4, truncado a k=2
]

"""

def build_pascal_table_k(n: int, k: int) -> List[List[int]]:
    """
    Construye tabla de Pascal hasta fila n limitada a columnas 0..min(i,k)
    tal que table[i][j] = C(i,j) para 0 <= i <= n y 0 <= j <= min(i,k).
    """

    # Inicializa estructura de tabla vacía
    table: List[List[int]] = []

    # Devuelve tabla completa
    return table
    

def solve_project_teams(n: int, k: int) -> Tuple[int, List[List[int]]]:
    """
    Calcula número de equipos C(n,k) y devuelve también tabla DP utilizada.
    Retorna una tupla (teams, table) donde teams = C(n,k).
    """

    teams: int = 0
    table: List[List[int]] = []

    # Pasos a seguir:
    # 1. Validar casos base
    # 2. Construir tabla DP: Tabla de Pascal (hasta n limitado por k)
    # 3. Extraer resultado C(n,k) desde tabla
    

    # 4. Devuelve número de equipos y tabla completa
    return teams, table
