# S4d: Punto de reunión (Grafos con BFS)

**Algoritmos y Programación**

- **Límite de entrega:** domingo, 11 de octubre de 2026, 23:59
- **Tipo de trabajo:** Individual
- **Ficheros requeridos:** `main.py`, `solve.py`, `minigraph.py`, `utils.py`, `simple_queue.py` (se descargan aparte)

## Contexto

Varias personas parten de diferentes posiciones (pudiendo haber varias personas en la misma posición) de una red de caminos bidireccionales (grafo no dirigido y sin pesos). Cada enlace (arista) representa un tramo y todos los tramos cuentan lo mismo. Se busca un punto de reunión donde la distancia que deba recorrer la persona más alejada sea lo más pequeña posible.

## Objetivo

Entre los caminos (lista de vértices) alcanzables por todas las personas, elegir el que minimice la mayor de las distancias mínimas desde sus posiciones iniciales (vértices).

Para un candidato `v`, habrá que calcular la distancia mínima desde cada posición hasta `v` y tomar la mayor. De entre todos los candidatos, se elige aquel con el menor valor de ese máximo, aclarando que **no se minimiza la suma ni la media** de las distancias.

> **NOTA:** Un candidato es un vértice que se está considerando como posible punto de reunión. No es una persona ni un camino.

Dicho de otra forma, elige como punto de reunión un vértice al que puedan llegar todas las personas. Para cada posible punto, calcula la distancia más corta desde la posición de cada persona y toma la mayor de esas distancias. El punto elegido será aquel cuya distancia máxima sea menor.

**Consideraciones:**

- Cualquier vértice puede ser punto de reunión, aunque no sea una posición inicial.
- También se permite reunirse en la posición inicial de alguna persona.
- En caso de empate, se elige el vértice de menor identificador numérico.
- Si no existe un vértice alcanzable por todos, se indica que no hay solución.

## Formato de entrada

```
N M K
p1 p2 ... pK
u1 v1
...
uM vM
```

donde:

- `N`: número de vértices, identificados con enteros desde 1 hasta N.
- `M`: número de aristas no dirigidas.
- `K`: número de personas.
- La segunda línea contiene exactamente `K` posiciones iniciales, donde se permiten repeticiones porque varias personas pueden partir del mismo vértice, pero el orden de las personas no afecta al resultado.
- Las siguientes `M` líneas contienen una arista no dirigida `u v`.

**Consideraciones:**

- Se cumple que N >= 1, M > 0 y K >= 1.
- Todos los identificadores pertenecen a 1..N.
- No hay bucles ni enlaces (aristas) repetidos.
- Puede haber ciclos, componentes desconectadas y vértices aislados.

## Formato de salida

La salida debe consistir en exactamente dos líneas:

```
Punto=P
DistanciaMaxima=D
```

donde:

- `P`: identificador del punto elegido.
- `D`: mayor distancia mínima desde las posiciones iniciales hasta P, medida en número de enlaces (aristas).

Si no existe un punto común alcanzable:

```
Punto=-1
DistanciaMaxima=-1
```

> **NOTA:** Si todas las personas están en el mismo vértice (nodo), ese es el punto elegido y D = 0, incluso si está aislado.

## Ejemplo de caso de prueba

**Entrada:**

```
7 5 2
1 5
1 2
2 3
3 4
4 5
6 7
```

**Salida esperada:**

```
Punto=3
DistanciaMaxima=2
```

**Explicación:** En el vértice 3 ambas personas recorren *dos tramos*. En 2 o en 4, alguna tendría que recorrer *tres tramos*. La **componente conexa** (grupo de vértices conectados entre sí, pero sin conexiones con los demás vértices del grafo) formada por 6 y 7 no contiene participantes, pero que esté aislada no impide la reunión.

**Ejemplo de empate:** En la cadena 1-2-3-4, con personas en 1 y 4, los puntos 2 y 3 tienen **distancia máxima** 2, por lo que se elige el punto 2 por su **menor identificador**.

**Diagrama (c03: N=4, M=3, K=2, personas en [4, 1] → Punto=2, DistanciaMaxima=2):**

Cadena lineal 1 — 2 — 3 — 4. Leyenda: naranja = posición inicial (vértices 1 y 4), verde = punto de reunión (vértice 2), azul = vértice (vértice 3).

## Tarea del alumno

Implementar la siguiente función en `solve.py`:

```python
def solve_punto_reunion(graph, positions):
    ...
```

**Parámetros:**

- `graph`: `Graph` (desde `minigraph.py`) **no dirigido y sin pesos**, ya construido con todos los vértices 1..N, incluidos los posibles aislados.
- `positions`: lista no vacía de posiciones iniciales, posiblemente repetidas.

**Resultado:** tupla de dos enteros `(punto, distancia_maxima)` que, en caso de no haber solución, devuelve `(-1, -1)`.

> **NOTA:** `main.py` lee los datos, construye el grafo, llama a la función a implementar y presenta la salida. Esta función a implementar **no debe leer ni imprimir**, ya que de eso se encarga `main.py`.

## Estrategia requerida

- Realiza **BFS** desde cada posición inicial distinta, usando `Queue` de `simple_queue.py` como cola FIFO.
- También se acepta repetir BFS para personas que comparten posición.
- Calcula el máximo de las distancias para cada candidato alcanzable por todos.
- Selecciona por menor distancia máxima y después por menor identificador numérico.
- No sustituyas las búsquedas por una única **BFS multiorigen**: esta calcularía la distancia al participante más cercano, no la distancia de cada participante.
