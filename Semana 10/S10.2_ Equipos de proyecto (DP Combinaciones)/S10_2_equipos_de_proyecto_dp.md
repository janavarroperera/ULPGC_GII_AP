# S10.2: Equipos de proyecto (DP Combinaciones)

- **Límite de entrega:** domingo, 22 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `utils.py`
- **Número máximo de ficheros:** 4
- **Tipo de trabajo:** Individual

## Contexto

Imagina que en una clase hay 10 alumnos y se deben formar grupos de 3 alumnos (por equipo) para un trabajo de laboratorio. ¿Cuántos equipos distintos pueden formarse?

Para formar equipos de 3 sin importar el orden ni permitir repeticiones, el número de equipos posibles viene dado por el Coeficiente Binomial:

```
C(n,k) = n! / (k! (n-k)!)
```

Aplicando al caso del enunciado (n=10, k=3):

```
C(10,3) = (10 × 9 × 8) / (3 × 2 × 1) = 120
```

Por tanto, pueden formarse **120 equipos distintos**.

## Objetivo

Generalizar el cálculo para cualquier `n` (alumnos) y `k` (tamaño del equipo), y construir la tabla DP (usando el Triángulo de Pascal) utilizada para obtener C(n,k):

1. Calcular C(n,k) como el número de equipos posibles.
2. Construir la tabla DP hasta `n` y rellenar las filas (solo columnas `0..min(i,k)` por fila, suficientes para obtener C(n,k)).

## Formato de entrada

Una única línea con dos valores enteros:

```
n k
```

donde `n` y `k` son enteros, con `0 ≤ k ≤ n ≤ 30` (para limitar combinaciones).

## Formato de salida

Varias líneas con el siguiente formato:

```
Teams=VALUE
DP_Table:
row 0: 1
row 1: 1 1
row 2: 1 2 1
...
row n: 1 ... C(n,k)
```

donde:

- Primera línea: `VALUE` es el valor de C(n,k).
- Siguientes `n+1` líneas: se incluye la tabla con las filas `0..n`; en cada fila `i` se muestran las columnas `0..min(i,k)`.

## Ejemplo de caso de prueba

**Entrada:**

```
10 3
```

**Salida esperada** (se muestra parcialmente en el enunciado):

```
Teams=120
DP_Table:
row 0: 1
row 1: 1 1
row 2: 1 2 1
...
row 10: 1 10 45 120
```

### Diagrama explicativo (Caso c01: entrada "10 3", 10 alumnos, equipos de 3)

Resultado: Teams = C(10,3) = 120. El diagrama muestra la tabla DP con filas `i = 0..10` y columnas `j = 0..3`:

| i \ j | j=0 | j=1 | j=2 | j=3 |
|:-----:|:---:|:---:|:---:|:---:|
| **i=0**  | 1 | — | — | — |
| **i=1**  | 1 | 1 | — | — |
| **i=2**  | 1 | 2 | 1 | — |
| **i=3**  | 1 | 3 | 3 | 1 |
| **i=4**  | 1 | 4 | 6 | 4 |
| **i=5**  | 1 | 5 | 10 | 10 |
| **i=6**  | 1 | 6 | 15 | 20 |
| **i=7**  | 1 | 7 | 21 | 35 |
| **i=8**  | 1 | 8 | 28 | 56 |
| **i=9**  | 1 | 9 | **36** | **84** |
| **i=10** | 1 | 10 | 45 | **120** |

Leyenda del diagrama original (colores):

- **Naranja:** C(10,3) = 120 (resultado), celda `(i=10, j=3)`.
- **Azul:** C(9,2) + C(9,3) = 36 + 84, las dos celdas de la fila `i=9` que se suman para obtener el resultado (flechas hacia la celda del resultado).
- **Verde claro:** caso base, C(i,0) = C(i,i) = 1 (columna `j=0` y diagonal `j=i`).
- **Gris (marcadas con "—" arriba):** fuera de la tabla (`j > i`).

## Tarea del alumno

Implementar en `solve.py` las siguientes funciones:

- `build_pascal_table_k(n, k) -> list[list[int]]`
  - Construye la **tabla DP de coeficientes binomiales** (Triángulo de Pascal) hasta la fila `n`.
  - Cada fila `i` debe contener exactamente las columnas `j = 0..min(i, k)`.
  - **Recurrencia:** `C(i,0)=C(i,i)=1` y `C(i,j)=C(i-1,j-1)+C(i-1,j)`.

- `solve_project_teams(n, k) -> tuple[int, list[list[int]]]`
  - Debe construir la **tabla DP** usando `build_pascal_table_k()` y devolver `(teams, table)` donde `teams = table[n][k]`.
  - **Casos base** a manejar:
    - Si `k == 0` o `k == n`, el resultado debe ser `1` y la tabla coherente con esa fila.
    - Si `k < 0` o `k > n`, devuelve `(0, [[1]])` (no se darán en este ejercicio).

**Ficheros requeridos:** `main.py`, `solve.py`, `utils.py` (se descargan aparte con el botón "Descargar").
