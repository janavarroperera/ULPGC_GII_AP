# S5.4: Problema del Submarino (Backtracking)

- **Límite de entrega:** domingo, 18 de octubre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `minigraph.py`, `simple_queue.py`, `simple_stack.py`, `utils.py`
- **Tipo de trabajo:** Individual

## Contexto

Estamos atrapados en un submarino averiado en una red de cuevas submarinas y necesitamos calcular todas las rutas posibles para escapar.

Las cuevas están conectadas por túneles que se pueden recorrer en ambos sentidos y hay dos tipos:

- **Cuevas grandes:** sus nombres están escritos en MAYÚSCULAS y se pueden visitar tantas veces como se desee durante una ruta.
- **Cuevas pequeñas:** sus nombres están escritos en minúsculas y solo se pueden visitar una vez en cada ruta.

## Objetivo

- Encontrar todas las rutas válidas desde `start` hasta `end` respetando las restricciones de visita anteriores.
- Devolver cada ruta como una lista con los nombres de las cuevas en el orden recorrido.
- Calcular el número total de rutas válidas.

**NOTA:** No se puede regresar a `start`, puesto que también es una cueva pequeña.

## Formato de entrada

La entrada de datos tiene el siguiente formato:

```
N
cueva1-cueva2
...
```

donde:

- La primera línea contiene un entero `N`, que indica el número de túneles.
- Las siguientes `N` líneas describen un túnel (cada una mediante los nombres de dos cuevas separados por un guion).

Cada conexión es bidireccional: `A-b` permite ir de `A` a `b` y de `b` a `A`. Las mayúsculas y minúsculas de los nombres determinan el tipo de cueva y deben conservarse.

## Formato de salida

Se muestra una ruta por línea, con el formato de una lista (de cadenas de texto) de Python donde cada lista incluye las cuevas `start` y `end`. Las rutas se muestran ordenadas:

1. Por longitud creciente, es decir, por el número de cuevas de la lista.
2. En caso de igual longitud, por orden lexicográfico de las listas, según la comparación de cadenas de Python.

La última línea contiene únicamente el número total de rutas válidas. Si no hay ninguna ruta válida, se imprime `0`.

## Ejemplo de caso de prueba

**Entrada:**

```
7
start-A
start-b
A-c
A-b
b-d
A-end
b-end
```

**Salida esperada:**

```
['start', 'A', 'end']
['start', 'b', 'end']
['start', 'A', 'b', 'end']
['start', 'b', 'A', 'end']
['start', 'A', 'b', 'A', 'end']
['start', 'A', 'c', 'A', 'end']
['start', 'A', 'c', 'A', 'b', 'end']
['start', 'b', 'A', 'c', 'A', 'end']
['start', 'A', 'b', 'A', 'c', 'A', 'end']
['start', 'A', 'c', 'A', 'b', 'A', 'end']
10
```

En este ejemplo hay 10 rutas válidas donde la cueva grande `A` puede aparecer varias veces en una ruta, mientras que las cuevas pequeñas no pueden repetirse.

**NOTA:** Ninguna ruta válida incluye `d`, porque para salir de ella sería necesario volver a visitar `b`.

**Diagrama (Submarino · Caso 01 / test1, "ejemplo del README"):** 6 cuevas, 7 túneles bidireccionales, 10 rutas válidas.

- Cuevas: `start`, `end`, `b`, `c`, `d` (pequeñas, una visita por ruta) y `A` (grande, puede repetirse).
- Túneles: `start-A`, `start-b`, `A-c`, `A-b`, `b-d`, `A-end`, `b-end`.
- Las rutas válidas se listan en el orden indicado (número de cuevas y después lexicográfico), numeradas del 01 al 10, con el mismo contenido que la salida esperada anterior. Total de la salida esperada: 10.
- Ruta 10 de 10 resaltada, una de las rutas que debe devolver `solve`: `start → A → c → A → b → A → end`.
- El orden y las repeticiones se leen en la secuencia; las líneas del grafo representan túneles sin dirección.
- La cueva `d` no aparece en ninguna ruta válida: para salir de ella habría que repetir `b`.

## Tarea del alumno

Implementar la siguiente función en `solve.py`:

```python
def solve(input_list):
    ...
```

**Parámetro:** `input_list`: lista de cadenas de texto con las **conexiones**, por ejemplo, `['start-A', 'start-b', 'A-end']`.

**NOTA:** En este ejercicio **no se incluye** la primera línea con el número de túneles.

**Resultado:** Una **tupla** `(num_solutions, solutions_list)` donde `num_solutions` debe coincidir con `len(solutions_list)`:

- `num_solutions` es un entero con el **número total de rutas válidas**.
- `solutions_list` es una lista de rutas donde cada ruta es una **lista de nombres de cuevas** desde `start` hasta `end`.

**NOTA:** La función debe devolver los resultados, no imprimirlos. Tampoco es necesario **ordenar** las rutas dentro de `solve`, ya que esa tarea la realiza `main.py`.

## Estrategia requerida

El enfoque a seguir para resolver este ejercicio es una **búsqueda en profundidad (DFS) con Backtracking**:

1. Iniciar la exploración en `start`, con una ruta que contenga esa cueva.
2. Explorar los vecinos de la cueva actual, descartando las cuevas pequeñas que ya estén en la ruta.
3. Permitir nuevas visitas a las cuevas grandes.
4. Al alcanzar `end`, guardar la ruta y no continuar explorando desde la salida.
5. Retroceder para explorar las demás alternativas.

## Pistas y consideraciones

- Para trabajar con la red de cuevas submarinas, utiliza un **grafo no dirigido de MiniGraph** donde se puede añadir los túneles con `add_edge` y consultar las cuevas adyacentes con `neighbors`.
- Puedes utilizar `nombre.islower()` para identificar una cueva pequeña.
- Si modificas una misma lista durante la exploración, **guarda una copia** al encontrar una solución para que el retroceso no altere las rutas ya almacenadas.
- No busques únicamente el camino más corto, se piden todas las rutas válidas.
- No marques permanentemente las cuevas grandes como visitadas, porque se permite repetirlas.
