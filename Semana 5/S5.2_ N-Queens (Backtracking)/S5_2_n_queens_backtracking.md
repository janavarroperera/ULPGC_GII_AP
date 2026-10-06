# S5.2: N-Queens (Backtracking)

- **Límite de entrega:** domingo, 18 de octubre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `utils.py` (número máximo de ficheros: 4)
- **Tipo de trabajo:** Individual

## Contexto

El problema de las N reinas consiste en colocar N reinas en un tablero de ajedrez de N × N casillas sin que ninguna ataque a otra. Por tanto, dos reinas no pueden compartir fila, columna ni diagonal.

En este ejercicio se resolverá el problema mediante un recorrido en profundidad (DFS) con vuelta atrás (Backtracking). El programa debe generar exactamente las mismas soluciones que la versión mediante fuerza bruta, pero descartando las colocaciones parciales no válidas antes de completarlas.

## Objetivo

Encontrar todas las disposiciones válidas de las N reinas mediante Backtracking y devolverlas como una lista de listas:

- Cada solución se representa mediante un vector `row` de longitud N, donde `row[c]` indica la fila de la reina situada en la columna `c`.
- Las filas y columnas se numeran desde 0 hasta N - 1.

## Formato de entrada

La entrada estándar contiene una única línea con el número entero `N`. Este valor indica tanto el número de reinas como el número de filas y columnas del tablero. El formato es el mismo que en la versión mediante fuerza bruta.

## Formato de salida

Se imprime una solución por línea, con el formato de una lista de Python: valores separados por coma y espacio, entre corchetes.

```
[fila_columna_0, fila_columna_1, ..., fila_columna_N-1]
```

**NOTA:** Deben aparecer todas las soluciones válidas (sin duplicados) y, para seguir el orden de salida requerido, se deben recorrer las columnas de izquierda a derecha y probar las filas en orden creciente, desde 0 hasta N - 1.

Si no existen soluciones, la función devuelve una lista vacía y el programa no imprime ninguna línea de soluciones.

## Ejemplo de caso de prueba

**Entrada:**

```
4
```

**Salida esperada:**

```
[1, 3, 0, 2]
[2, 0, 3, 1]
```

La entrada corresponde a 4 reinas en un tablero de 4 × 4. En la primera solución, las reinas ocupan las filas 1, 3, 0 y 2 en las columnas 0, 1, 2 y 3, respectivamente.

**Diagrama (Caso 01 · Q4, entrada N = 4):** 4 reinas en un tablero 4 × 4, 2 soluciones en total. Las filas y columnas comienzan en 0; cada Q representa una reina.

- **Solución 1 de 2**, `row = [1, 3, 0, 2]`: reinas en (fila 1, col 0), (fila 3, col 1), (fila 0, col 2), (fila 2, col 3).
- **Solución 2 de 2**, `row = [2, 0, 3, 1]`: reinas en (fila 2, col 0), (fila 0, col 1), (fila 3, col 2), (fila 1, col 3).

## Tarea del alumno

Implementar en `solve.py` la función que calcula todas las soluciones mediante **Backtracking**.

```python
def solve(num_queens):
    ...
```

La función debe:

- Recibir el número de reinas, `num_queens`.
- Devolver una lista de listas con todas las **soluciones válidas**.
- Representar cada **solución con índices de fila** desde 0 hasta `num_queens - 1`, colocando una **reina por columna**.
- Aplicar un **recorrido DFS recursivo con poda** de las **soluciones parciales** que incumplan las restricciones.
- Continuar la búsqueda después de encontrar una solución, hasta explorar todas las posibilidades válidas.

La diferencia respecto a la **fuerza bruta** es que no se generan todas las configuraciones completas para validarlas después: las ramas incompatibles se descartan en cuanto se detecta el conflicto.

**NOTA:** De la lectura de la entrada y el formateo de los resultados ya se encarga `main.py`.

## Estrategia requerida

1. Mantener un vector que represente la colocación de las reinas. Puede inicializarse con N valores -1 para indicar posiciones todavía no ocupadas.
2. Definir un recorrido recursivo `dfs(level)`, donde `level` indica cuántas reinas se han colocado y cuál es la siguiente columna que se debe explorar.
3. Comprobar la validez de la solución parcial formada por las posiciones 0 a `level - 1`. Si dos reinas comparten fila o diagonal, detener esa rama y retroceder.
4. Si `level == N` y la colocación es válida, guardar una copia de la solución y regresar para continuar la búsqueda.
5. En caso contrario, probar cada fila posible en la columna `level` y continuar recursivamente con `dfs(level + 1)`.
6. Iniciar el recorrido con `dfs(0)` y devolver la lista de soluciones al finalizar.

## Pistas y consideraciones

- Al colocar una reina por columna, la restricción de columnas distintas se cumple por construcción.
- Dos reinas situadas en las columnas `i` y `j` comparten fila si `row[i] == row[j]`.
- Comparten diagonal si `abs(row[i] - row[j]) == abs(i - j)`.
- Guarda una **copia** del vector al encontrar una solución: el recorrido seguirá modificando el mismo vector al explorar otras ramas.
- No detengas toda la búsqueda al encontrar la primera solución; se piden todas.
