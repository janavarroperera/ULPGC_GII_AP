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

  for i in range (0, n + 1):
    row = []

    for j in range(0, min(i, k) + 1):
      if j == 0 or j == i:
        row.append(1)
      else:
        row.append(table[i-1][j-1] + table[i-1][j])

    table.append(row)

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
  if (k < 0) or (k > n):
    return 0, [[1]]
  # 2. Construir tabla DP: Tabla de Pascal (hasta n limitado por k)
  table = build_pascal_table_k(n, k)
  # 3. Extraer resultado C(n,k) desde tabla
  teams = table[n][k]

  # 4. Devuelve número de equipos y tabla completa
  return teams, table
