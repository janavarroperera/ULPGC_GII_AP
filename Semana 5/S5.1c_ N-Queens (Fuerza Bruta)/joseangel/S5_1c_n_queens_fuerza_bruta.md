# S5.1c: N-Queens (Fuerza Bruta)

- **Límite de entrega:** domingo, 18 de octubre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `my_iterator.py`, `utils.py`
- **Tipo de trabajo:** Individual

## Contexto

El problema de las N reinas consiste en colocar N reinas en un tablero de ajedrez de N × N de forma que ninguna ataque a otra. Para ello, no puede haber dos reinas en la misma fila, columna o diagonal.

Este ejercicio corresponde a la última parte de una secuencia de tres partes:

1. Calcular el siguiente número a partir de su representación como una lista de dígitos en una base de numeración determinada.
2. Programar, utilizando `yield`, un iterador de combinaciones para resolver problemas mediante fuerza bruta.
3. Utilizar ese iterador para calcular todas las soluciones del problema de las N reinas.

## Objetivo

Calcular todas las disposiciones válidas de N reinas en un tablero de N × N, utilizando el iterador de los ejercicios anteriores y un enfoque de fuerza bruta:

- Cada solución se representa mediante una lista de N enteros.
- El valor de la posición `c` indica la fila en la que se coloca la reina de la columna `c`.
- Tanto las filas como las columnas se numeran desde 0 hasta N - 1.

Por ejemplo, `[2, 0, 3, 1]` representa una reina en cada una de estas posiciones:

- Columna 0, fila 2.
- Columna 1, fila 0.
- Columna 2, fila 3.
- Columna 3, fila 1.

## Formato de entrada

La entrada contiene una única línea con el valor entero `N`, que indica tanto el número de reinas como el número de filas y columnas del tablero.

## Formato de salida

Se imprime una solución por línea, usando el formato de una lista de Python: corchetes y valores separados por comas y espacios.

Deben mostrarse todas las soluciones, sin mensajes adicionales ni una lista exterior que las agrupe. Se conserva el **orden de generación del iterador**, que recorre las combinaciones en **orden numérico creciente en base N**.

Para N = 4, la salida es:

```
[1, 3, 0, 2]
[2, 0, 3, 1]
```

**NOTA:** Si no existen soluciones, la lista devuelta estará vacía y no se imprimirá ninguna línea.

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

Estas son las dos formas válidas de colocar cuatro reinas en un tablero de 4 × 4.

**Diagrama (Caso 01 · Q4 · N = 4):** entrada 4, 2 soluciones en el orden de salida. Cada lista indica la fila (desde 0) de la reina en cada columna (desde 0).

- **Solución 01:** `[1, 3, 0, 2]` → reinas en (fila 1, col 0), (fila 3, col 1), (fila 0, col 2), (fila 2, col 3).
- **Solución 02:** `[2, 0, 3, 1]` → reinas en (fila 2, col 0), (fila 0, col 1), (fila 3, col 2), (fila 1, col 3).

## Tarea del alumno

Reutilizar en `my_iterator.py` las soluciones de los dos ejercicios anteriores e implementar la función `solve()` en `solve.py`.

```python
def solve(num_queens):
    ...
```

donde:

- **Parámetro:** `num_queens`, número de reinas y tamaño del tablero cuadrado.
- **Retorno:** una lista de listas que contiene todas las soluciones válidas.

La función debe:

- Utilizar el iterador propio para generar las configuraciones candidatas.
- Comprobar que ninguna pareja de reinas comparte fila ni diagonal. La representación elegida ya garantiza una reina por columna.
- Añadir cada configuración válida a la lista de soluciones, sin duplicados.
- Devolver la lista completa con todas las soluciones, no solo la primera solución encontrada.
- Dejar la lectura de la entrada y la impresión de los resultados a `main.py`.

Por ejemplo, para `solve(4)` la función debe devolver:

```python
[[1, 3, 0, 2], [2, 0, 3, 1]]
```

Archivos principales:

- `main.py`: lee el valor de N, llama a `solve(num_queens)` e imprime cada solución devuelta. No es necesario modificarlo para resolver el ejercicio.
- `solve.py`: contiene la función que debe calcular y devolver todas las soluciones.
- `my_iterator.py`: contiene `next_number(digits, base)` y la clase `My_Iterator`, que deben reutilizarse de los ejercicios anteriores. El método `next()` genera las combinaciones mediante `yield`.
- `utils.py`: proporciona las utilidades de lectura utilizadas por `main.py`.

## Estrategia requerida

Aplicar fuerza bruta mediante el iterador de combinaciones:

1. Representar cada configuración mediante N dígitos en base N donde cada dígito indica la fila de una reina en su columna.
2. Crear un `My_Iterator` con `num_digits=num_queens` y `base=num_queens`.
3. Recorrer con su método `next()` las N^N configuraciones, desde `[0, 0, ..., 0]` hasta `[N - 1, N - 1, ..., N - 1]`.
4. Descartar las configuraciones que tengan reinas en una misma fila o diagonal.
5. Guardar las configuraciones válidas y devolverlas al finalizar el recorrido.

**NOTA:** El enfoque solicitado es generar y comprobar todas las configuraciones posibles.

## Pistas y consideraciones

- Dos reinas comparten fila si sus valores en la lista son iguales.
- Para dos columnas distintas `i` y `j`, las reinas comparten diagonal si `abs(filas[i] - filas[j]) == abs(i - j)`.
- No hace falta comprobar conflictos de columna: cada posición de la lista corresponde a una columna distinta.
- Si el iterador reutiliza y modifica una misma lista, guarda una copia al conservar una solución para evitar que cambie en las iteraciones posteriores.
- El iterador debe incluir tanto la primera como la última combinación y finalizar después de esta última.
