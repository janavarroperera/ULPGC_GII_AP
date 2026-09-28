# S4b: Grafos (DFS): Topological sort (recursivo e iterativo)

**Algoritmos y Programación**

- **Límite de entrega:** domingo, 11 de octubre de 2026, 23:59
- **Tipo de trabajo:** Individual
- **Ficheros requeridos:** `main.py`, `solve.py`, `graph_utils.py`, `minigraph.py`, `simple_stack.py`, `utils.py` (se descargan aparte)

## Contexto

Un orden topológico de un grafo dirigido acíclico (DAG) es una secuencia de sus vértices tal que, para toda arista (u, v), el vértice u aparece antes que v. Es útil para resolver problemas de dependencias: planificación de tareas, orden de compilación de módulos, prerrequisitos de asignaturas, etc.

En este ejercicio se trabaja con la librería MiniGraph (`minigraph.py`), una versión simplificada de NetworkX, para calcular un orden topológico válido aplicando un recorrido en profundidad (DFS).

## Objetivo

Implementar dos versiones del algoritmo que calcula un orden topológico válido en un grafo dirigido:

1. **Versión recursiva:** programar el algoritmo recursivo (explicado en clase).
2. **Versión iterativa:** diseñar y programar un algoritmo iterativo (con pila).

> **Nota:** La solución admite cualquier orden topológico válido; no es necesario que coincida con uno concreto.

## Formato de entrada

```
N M
u1 v1 w1
u2 v2 w2
...
uM vM wM
```

donde:

- **Primera línea:** `N` = número de vértices (que se numeran de 1 a N) y `M` = número de aristas.
- **Resto de líneas:** cada una describe una arista dirigida `u v w`, donde `u` es el origen, `v` el destino y `w` el peso (que no afecta al orden topológico, pero forma parte del formato de entrada).

## Formato de salida

Se imprime un diccionario Python `{posición: vértice}` ordenado por posición, donde la posición 1 corresponde al primer vértice del orden topológico:

```
{1: 4, 2: 5, 3: 6, 4: 1, 5: 2, 6: 3, ...}
```

## Ejemplo de caso de prueba

**Entrada:**

```
8 9
1 4 5
2 4 2
2 5 3
3 5 1
3 8 6
4 6 8
4 7 7
4 8 6
5 7 2
```

**Salida esperada (una posible):**

```
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
```

> **NOTA:** Cualquier orden topológico válido se considera correcto (puede haber múltiples alternativas aceptadas).

**Diagrama (c03 · Caso G3 · Orden topológico · «Ejemplo del README» · 8 vértices · 9 aristas dirigidas · Una solución válida entre varias posibles):**

Grafo original con la posición asignada a cada vértice (en cada nodo: vértice y posición; etiqueta de arista: peso, que no afecta al orden). En este ejemplo el vértice *i* recibe la posición *i*:

- 1 (pos. 1) → 4 (pos. 4), peso 5
- 2 (pos. 2) → 4 (pos. 4), peso 2
- 2 (pos. 2) → 5 (pos. 5), peso 3
- 3 (pos. 3) → 5 (pos. 5), peso 1
- 3 (pos. 3) → 8 (pos. 8), peso 6
- 4 (pos. 4) → 6 (pos. 6), peso 8
- 4 (pos. 4) → 7 (pos. 7), peso 7
- 4 (pos. 4) → 8 (pos. 8), peso 6
- 5 (pos. 5) → 7 (pos. 7), peso 2

Un orden topológico válido (secuencia de izquierda a derecha; no representa un camino de aristas): 1, 2, 3, 4, 5, 6, 7, 8 (posiciones 1 a 8). Salida `{posición: vértice}` (misma salida que el README):

```
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
```

Fuente: `vpl_evaluate.cases` · G3. Todas las aristas cumplen posición(origen) < posición(destino).

## Tarea del alumno

Implementar las siguientes funciones en `solve.py`:

```python
def dfs_topological_sort(graph):
    """Devuelve un dict {vértice: rango} con un orden topológico válido."""
```

La función debe:

- Retornar un diccionario `{vértice: posición}` que represente un orden topológico válido.
- Usar las funciones de **MiniGraph**: `graph.number_of_nodes()`, `graph.out_edges(u)`, etc.
- Para la **versión iterativa**, usar la clase `Stack` de `simple_stack.py`.

**Archivos principales:**

- `main.py`: lee la entrada estándar, construye el grafo y formatea/imprime la salida.
- `graph_utils.py`: contiene `build_digraph_with_weights(edges_list, num_nodes, num_edges)`, que construye el `nx.DiGraph()` de MiniGraph con los nodos 1..N y las aristas ponderadas.
- `solve.py`: contiene la función que el alumno debe completar.
- `simple_stack.py`: pila auxiliar (`Stack`) disponible para la versión iterativa.
