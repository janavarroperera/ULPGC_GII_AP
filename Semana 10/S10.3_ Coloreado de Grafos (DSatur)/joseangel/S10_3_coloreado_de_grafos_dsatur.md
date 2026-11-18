# S10.3: Coloreado de Grafos (DSatur)

- **Límite de entrega:** domingo, 22 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `utils.py`
- **Número máximo de ficheros:** 5
- **Tipo de trabajo:** Individual

## Contexto

Muchos problemas de asignación se pueden modelar mediante el coloreado de un grafo: asignar horarios a exámenes que comparten alumnos, frecuencias a antenas cercanas o registros a variables que están vivas al mismo tiempo. Cada elemento es un nodo y cada conflicto es una arista. Dos nodos unidos por una arista no pueden recibir el mismo color.

Encontrar el número mínimo de colores es un problema difícil, por lo que en la práctica se usan heurísticas voraces donde **DSatur** es una de las más conocidas: en lugar de colorear los nodos en un orden fijo, decide en cada paso qué nodo colorear a continuación según lo "restringido" que esté por sus vecinos ya coloreados.

## Objetivo

- Colorear todos los nodos de un grafo no dirigido de forma que dos nodos adyacentes nunca tengan el mismo color.
- Elegir el orden de coloreado y el color de cada nodo siguiendo las reglas de DSatur descritas más abajo.
- Devolver el color asignado a cada nodo, en el orden de los nodos 1..N.

## Formato de entrada

```
N M
u1 v1
u2 v2
...
uM vM
```

donde:

- `N`: número de nodos (`N ≥ 1`; los nodos se numeran de 1 a N).
- `M`: número de aristas (`M ≥ 0`).
- Cada una de las `M` líneas siguientes contiene una arista no dirigida entre los nodos `u` y `v` (`1 ≤ u, v ≤ N`, `u ≠ v`).

**NOTA:** Se considera que no hay aristas repetidas (pero puede haber nodos sin aristas) y todos los nodos de 1 a N forman parte del grafo.

## Formato de salida

Una única línea con la lista de colores, tal como la imprime Python:

```
[c1, c2, ..., cN]
```

donde:

- `ci` es el color asignado al nodo `i` (la lista sigue el orden de los nodos `1, 2, ..., N`, **no** el orden en que se han coloreado).
- Los colores son valores enteros que **empiezan en 0** (`0, 1, 2, ...`).

## Ejemplo de caso de prueba

**c01 | Case 1: Grafo rueda** — 7 nodos · 12 aristas · grafo no dirigido · 3 colores usados.

**Entrada:**

```
7 12
1 2
2 3
3 4
4 5
5 6
6 1
7 1
7 2
7 3
7 4
7 5
7 6
```

**Salida:**

```
[1, 2, 1, 2, 1, 2, 0]
```

**Orden de coloreado DSatur:** 7 → 1 → 2 → 3 → 4 → 5 → 6

(Única salida admitida en `vpl_evaluate.cases`.)

### Diagrama explicativo

El diagrama muestra el grafo coloreado (etiqueta: nodo / color). Es una rueda: los nodos 1..6 forman un ciclo exterior (1-2-3-4-5-6-1) y el nodo central 7 está unido a todos ellos. Colores finales:

| Nodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:----:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Color | 1 | 2 | 1 | 2 | 1 | 2 | 0 |

Leyenda: color 0 (azul), color 1 (naranja), color 2 (verde).

### Explicación

El grafo es una rueda con un ciclo 1-2-3-4-5-6-1 y un nodo central 7 unido a todos los demás.

1. Ningún nodo está coloreado, así que todos tienen saturación 0. El nodo 7 tiene el mayor grado (6) y recibe el color 0.
2. Los nodos 1..6 tienen ahora saturación 1 y grado 3. Se desempata por el menor identificador: el nodo 1 recibe el color 1.
3. Los nodos 2 y 6 tienen saturación 2 (ven los colores 0 y 1). Se elige el 2, que recibe el color 2.
4. Se continúa igual con 3 (color 1), 4 (color 2), 5 (color 1) y 6 (color 2).

El resultado usa 3 colores, el mínimo posible para una rueda con un ciclo de longitud par.

## Tarea del alumno

Implementar la función `solve_dsat_coloring` en `solve.py`.

```python
def solve_dsat_coloring(graph, order_nodes):
    """Colorea el grafo con DSatur y devuelve la lista de colores."""
```

donde:

- `graph`: grafo no dirigido de NetworkX (`nx.Graph`) ya construido por `main.py`, con los nodos `1..N` y sus aristas, donde se pueden consultar los vecinos de un nodo con `graph.neighbors(u)` y su grado con `graph.degree(u)`.
- `order_nodes`: iterable con los nodos del grafo en el orden `1, 2, ..., N`. **No** es el orden de coloreado sino que sirve para indexar el resultado.

La función debe retornar una lista de enteros con el color de cada nodo, en el mismo orden que `order_nodes`. El `main.py` ya prepara esta lista a partir del diccionario `nodes_colors`; basta con asignar el color de cada nodo en ese diccionario.

### Algoritmo DSatur (*Degree of Saturation*)

- La **saturación** de un nodo es el número de colores **distintos** que tienen sus vecinos ya coloreados.
- En cada paso se colorea un nodo todavía sin color, elegido así:
  1. El de **mayor saturación**.
  2. En caso de empate, el de **mayor grado** en el grafo.
  3. Si sigue habiendo empate, el de **menor identificador**.
- Al nodo elegido se le asigna el **menor color** (empezando en 0) que no use ninguno de sus vecinos.
- El proceso termina cuando **todos** los nodos tienen color.

**NOTA:** El algoritmo debe implementarse a mano y **no** está permitido usar las funciones de coloreado de NetworkX (por ejemplo, `nx.greedy_color` o `nx.coloring`).

**Ficheros requeridos:** `main.py`, `solve.py` (más `utils.py`, que se descarga aparte con el botón "Descargar").
