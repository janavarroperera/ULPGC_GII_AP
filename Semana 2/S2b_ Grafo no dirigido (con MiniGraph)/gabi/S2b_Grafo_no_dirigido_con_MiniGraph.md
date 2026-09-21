# Algoritmos y Programación — S2b: Grafo no dirigido (con MiniGraph)

**Límite de entrega:** domingo, 27 de septiembre de 2026, 23:59
**Ficheros requeridos:** `main.py`, `solve.py`, `minigraph.py`, `utils.py`
**Tipo de trabajo:** Individual

## Contexto

En este ejercicio se trabaja con la representación de grafos mediante el módulo `MiniGraph` (en `minigraph.py`), una versión reducida y simplificada de algunas operaciones habituales de NetworkX. El objetivo es construir un grafo no dirigido a partir de un fichero de entrada que describe sus vértices y aristas.

El programa principal (`main.py`) se encarga de leer la entrada, llamar a la función que construye el grafo y mostrar por pantalla un resumen del grafo resultante.

## Objetivo

Implementar la construcción de un grafo no dirigido usando MiniGraph.

Dado:

- El número de vértices del grafo.
- El número de aristas.
- La lista de aristas.

Se debe crear un objeto `nx.Graph()` que contenga:

- Todos los vértices numerados desde 1 hasta `num_nodes`.
- Todas las aristas indicadas en la entrada.

Para ello deben utilizarse algunas de las operaciones principales de MiniGraph:

- `nx.Graph()`
- `G.add_node()`
- `G.add_edge()`

## Formato de entrada

La entrada estándar tiene el siguiente formato:

```
N M
u1 v1
u2 v2
...
uM vM
```

donde:

- `N` es el número de vértices del grafo.
- `M` es el número de aristas del grafo.
- Cada una de las siguientes `M` líneas contiene dos enteros `u v`, que representan una arista no dirigida entre los vértices `u` y `v`. Los vértices se numeran desde 1 hasta `N`.

## Formato de salida

El programa debe imprimir exactamente cuatro líneas con la información del grafo construido:

```
Number of nodes: N
Nodes: [lista_de_vertices]
Number of edges: M
Edges: [lista_de_aristas]
```

La salida la genera `main.py` a partir del grafo devuelto por la función del alumno. La comparación en VPL es literal, por lo que los espacios, comas, corchetes y saltos de línea deben coincidir con el formato esperado.

## Ejemplo de caso de prueba

**Entrada:**

```
9 11
1 4
2 8
3 6
4 7
5 2
6 9
7 1
8 5
8 6
9 7
9 3
```

**Salida esperada:**

```
Number of nodes: 9
Nodes: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Number of edges: 11
Edges: [(1, 4), (2, 8), (3, 6), (4, 7), (5, 2), (6, 9), (7, 1), (8, 5), (8, 6), (9, 7), (9, 3)]
```

Junto con el ejemplo, el enunciado incluye un diagrama del grafo resultante, titulado "grafo_no_dirigido_basico" (9 vértices, 11 aristas). Muestra los nueve vértices numerados del 1 al 9 conectados según las aristas de la entrada, formando una cadena principal 1–4–7–9 que se ramifica hacia 3–6 y hacia 8, y desde 8 hacia 2–5 y hacia 6, ilustrando visualmente la misma estructura descrita en la salida esperada.

## Tarea del alumno

El alumno debe completar la función `build_graph` en `solve.py`.

**Archivos principales:**

- `main.py`: lee la entrada, obtiene `num_nodes`, `num_edges` y la lista de aristas, llama a `build_graph` y formatea la salida.
- `solve.py`: contiene la función que debe construir y devolver el grafo.
- `minigraph.py`: proporciona la clase `Graph` y sus operaciones básicas.
- `utils.py`: proporciona funciones auxiliares para la lectura de entrada.

**Función a implementar:**

```python
def build_graph(edges_list, num_nodes, num_edges):
    """Construye/devuelve grafo no dirigido a partir de lista de aristas."""
```

La función recibe:

- `edges_list`: lista de cadenas, donde cada cadena tiene el formato `"u v"`.
- `num_nodes`: número total de vértices.
- `num_edges`: número total de aristas.

La función debe devolver:

- Un objeto `nx.Graph()` con los vértices y aristas correspondientes.

**Tareas de la función a implementar:**

Debe:

- Crear un grafo no dirigido con `nx.Graph()`.
- Añadir todos los vértices desde 1 hasta `num_nodes` usando `add_node`.
- Procesar cada arista de `edges_list`.
- Convertir los extremos de cada arista a enteros.
- Añadir cada arista al grafo usando `add_edge`.
- Devolver el grafo construido.

No debe:

- Leer datos de teclado o de ficheros dentro de `solve.py`.
- Imprimir resultados dentro de `solve.py`.
- Modificar el formato de salida de `main.py`.

### Pistas y consideraciones

- La numeración de los vértices debe comenzar en 1, no en 0.
- Aunque un vértice no aparezca en ninguna arista, debe añadirse igualmente al grafo.
- `edges_list` contiene cadenas de texto, no tuplas de enteros.
- En un grafo no dirigido, una arista `u v` conecta ambos vértices sin orientación.
- Consulta la documentación inicial de `minigraph.py` para ver las operaciones disponibles.
