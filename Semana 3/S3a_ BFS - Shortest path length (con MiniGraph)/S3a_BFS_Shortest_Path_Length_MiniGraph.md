# S3a: BFS - Shortest Path Length (con MiniGraph)

**Límite de entrega:** domingo, 4 de octubre de 2026, 23:59
**Ficheros requeridos:** main.py, solve.py, simple_queue.py, graph_utils.py, minigraph.py, utils.py
**Tipo de trabajo:** Individual

## Contexto

En un grafo no dirigido y sin pesos, la distancia entre dos vértices es el número mínimo de aristas (o saltos) que hay que recorrer para llegar de uno a otro. Cada arista representa un salto y puede recorrerse en ambos sentidos.

El recorrido en anchura, BFS (Breadth-First Search), permite calcular estas distancias desde un vértice de origen, explorando primero sus vecinos y después los vértices situados a dos saltos, a tres saltos, etc.

> **NOTA:** En este ejercicio es obligatorio utilizar el módulo `minigraph.py` para representar el grafo y la cola de `simple_queue.py` para realizar el recorrido.

## Objetivo

- Construir un grafo no dirigido y sin pesos a partir de una lista de aristas.
- Implementar el algoritmo Shortest Path Length mediante BFS (explicado en clase de teoría).
- Calcular la distancia mínima, en número de saltos, desde el vértice 1 hasta todos los vértices del grafo.
- Devolver un diccionario que asocie cada vértice con su distancia al origen.

## Formato de entrada

La entrada de datos tiene el siguiente formato:

```
N M
u1 v1
u2 v2
... uM vM
```

La primera línea contiene dos enteros separados por espacios:

- **N**: número de vértices del grafo.
- **M**: número de aristas del grafo.

Los vértices se numeran desde 1 hasta N y el grafo contiene al menos el vértice de origen.

Cada una de las siguientes M líneas contiene los dos extremos "u v" de una arista, con u >= 1 y v >= 1. Las aristas son no dirigidas: una línea "u v" permite desplazarse tanto de u a v como de v a u. No es necesario escribir también la arista inversa.

No se proporcionan pesos: todas las aristas cuentan como un salto.

> **NOTA:** El origen no aparece en una línea adicional ya que `main.py` utiliza siempre el vértice 1.

## Formato de salida

Se imprime una única línea con un diccionario de Python que contiene las distancias, con las claves ordenadas de menor a mayor:

```
{1: 0, 2: distancia_2, ..., N: distancia_N}
```

donde:

- Los nombres `distancia_2`, `distancia_N` y los puntos suspensivos representan los valores correspondientes; no se imprimen literalmente.
- La distancia del origen a sí mismo es 0.
- Cada distancia indica el número mínimo de aristas del camino desde el origen hasta ese vértice, no el número de vértices del camino ni su orden de visita.
- Si un vértice no es alcanzable, su distancia se representa con el valor entero `sys.maxsize`, importado como `infinite` en `solve.py`. No se imprime la palabra "infinite".

> **NOTA:** El formateo y la salida de los datos corresponden a `main.py`. Las funciones del alumno solo deben devolver los resultados.

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
{1: 0, 2: 5, 3: 3, 4: 1, 5: 5, 6: 3, 7: 1, 8: 4, 9: 2}
```

Desde el vértice 1, los vértices se alcanzan por niveles:

- Distancia 0: 1.
- Distancia 1: 4 y 7.
- Distancia 2: 9.
- Distancia 3: 3 y 6.
- Distancia 4: 8.
- Distancia 5: 2 y 5.

Por ejemplo, el camino 1 → 7 → 9 → 6 → 8 → 2 alcanza el vértice 2 en cinco saltos.

*(El enunciado incluye además un diagrama del grafo con el vértice 1 resaltado como origen y cada vértice etiquetado con su distancia mínima en saltos (d = 0 a d = 5), ilustrando visualmente los niveles descritos arriba: nivel d=0 → vértice 1; d=1 → vértices 4 y 7; d=2 → vértice 9; d=3 → vértices 3 y 6; d=4 → vértice 8; d=5 → vértices 2 y 5.)*

## Tarea del alumno

Implementar las siguientes funciones, respetando sus nombres y parámetros.

### Parte 1: Construcción del grafo en `graph_utils.py`

```python
def build_graph(edges_list, num_nodes, num_edges):
    ...
```

**Parámetros:**

- `edges_list`: lista de `num_edges` cadenas; cada cadena contiene los extremos de una arista, por ejemplo, `"1 4"`.
- `num_nodes`: número de vértices.
- `num_edges`: número de aristas de la entrada.

**Resultado:** un grafo `Graph` de MiniGraph, no dirigido y sin pesos, con los vértices 1 a `num_nodes` y las aristas indicadas. Deben incluirse también los vértices que no tengan aristas.

### Parte 2: Cálculo de distancias en `solve.py`

```python
def bfs_path_length(graph, first_node):
    ...
```

**Parámetros:**

- `graph`: grafo no dirigido y sin pesos construido previamente.
- `first_node`: vértice de origen (en este ejercicio, `main.py` le pasa el valor 1).

**Resultado:** un diccionario `{vertice: distancia}` con una entrada para cada vértice del grafo, donde el origen tendrá distancia 0 y los vértices no alcanzables conservarán el valor `infinite` (`sys.maxsize`).

### Archivos principales

- **main.py**: lee la entrada, llama a `build_graph`, invoca `bfs_path_length`, ordena el diccionario por sus claves e imprime la salida.
- **graph_utils.py**: contiene la función de construcción del grafo que debes implementar.
- **solve.py**: contiene la función de cálculo de distancias que debes implementar.
- **minigraph.py**: proporciona la representación del grafo y operaciones como `Graph()`, `add_node`, `add_edge`, `nodes` y `neighbors`.
- **simple_queue.py**: proporciona la clase `Queue`, con los métodos `enqueue`, `dequeue` e `isEmpty`.
- **utils.py**: proporciona las funciones auxiliares de lectura.
- **vpl_evaluate.cases**: contiene las entradas y salidas esperadas de las pruebas.

> **NOTA:** Utiliza la clase `Queue` de `simple_queue.py`. Se trata de una cola donde los vértices deben procesarse en el orden en que se incorporan para mantener la exploración por niveles.

### Estrategia requerida

Utiliza un recorrido en anchura (BFS) con una cola FIFO:

1. Inicializa las distancias de los vértices y establece la del origen en 0.
2. Introduce el origen en la cola y registra que ya ha sido descubierto.
3. Mientras la cola no esté vacía, extrae un vértice y examina sus vecinos.
4. Al descubrir un vecino por primera vez, asigna su distancia a partir de la del vértice actual y añádelo a la cola.
5. Devuelve el diccionario de distancias al terminar el recorrido.

### Pistas y consideraciones

- Puedes recorrer los vecinos de un vértice mediante `graph.neighbors(vertice)`.
- Marca cada vértice como descubierto cuando lo añadas a la cola, para evitar incorporarlo varias veces.
- No sobrescribas una distancia ya calculada al encontrar otra arista hacia un vértice descubierto.
- Añade todos los vértices al construir el grafo, no solo los que aparecen en alguna arista.
- No necesitas guardar los caminos completos: el ejercicio pide únicamente sus longitudes.
- No necesitas ordenar el diccionario en `solve.py` ya que `main.py` se encarga del orden de impresión.
