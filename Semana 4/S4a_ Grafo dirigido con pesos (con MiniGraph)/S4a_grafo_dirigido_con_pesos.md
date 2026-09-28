# S4a: Grafo dirigido con pesos (con MiniGraph)

**Algoritmos y Programación**

- **Límite de entrega:** domingo, 11 de octubre de 2026, 23:59
- **Disponible desde:** lunes, 28 de septiembre de 2026, 08:57
- **Tipo de trabajo:** Individual
- **Ficheros requeridos:** `main.py`, `solve.py`, `minigraph.py`, `utils.py` (se descargan aparte)

## Contexto

Un grafo dirigido con pesos permite representar conexiones que tienen un sentido y un valor asociado. Cada arista une un vértice de origen con uno de destino, y su peso puede representar, por ejemplo, un coste o una distancia.

En este ejercicio se pide construir un grafo de este tipo utilizando el módulo MiniGraph proporcionado. Los datos de entrada describen el número de vértices y las aristas con sus respectivos pesos.

## Objetivo

- Crear un grafo dirigido con los vértices numerados desde 1 hasta `num_nodes`, ambos incluidos.
- Incorporar las aristas indicadas en la entrada, respetando su dirección y su peso.
- Devolver el grafo construido para que el programa principal muestre sus vértices y aristas.

> **NOTA:** En este ejercicio no se pide calcular caminos mínimos ni realizar recorridos: el objetivo es construir correctamente el grafo.

## Formato de entrada

La entrada describe un único grafo:

```
num_nodes num_edges
origen_1 destino_1 peso_1
...
origen_M destino_M peso_M
```

donde:

1. La primera línea contiene dos enteros separados por espacios:
   - `num_nodes`: número de vértices del grafo.
   - `num_edges`: número de aristas que se van a leer (M).
2. Las siguientes `num_edges` líneas contienen tres enteros separados por espacios: `origen destino peso`.
   - `origen` y `destino` son identificadores de vértices entre 1 y `num_nodes`.
   - `peso` es el valor asociado a la arista dirigida de `origen` a `destino`.

**Consideraciones:**

- La arista `origen destino peso` (que va desde origen hasta destino) no implica que exista también la arista inversa.
- Deben incluirse todos los vértices declarados, aunque alguno no aparezca en ninguna arista.

## Formato de salida

El programa principal imprime exactamente cuatro líneas:

```
Number of nodes: N
Nodes: [1, 2, ..., N]
Number of edges: M
Edges: [(origen, destino, {'weight': peso}), ...]
```

donde N y M representan el número de vértices y aristas del grafo construido.

**Consideraciones:**

- Los puntos suspensivos son únicamente explicativos y no se imprimen.
- Después de `Number of nodes:` y `Number of edges:` hay un espacio. Después de `Nodes:` y `Edges:` hay dos espacios.
- La lista de aristas se imprime completa en una sola línea.

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

**Salida esperada:**

```
Number of nodes: 8
Nodes:  [1, 2, 3, 4, 5, 6, 7, 8]
Number of edges: 9
Edges:  [(1, 4, {'weight': 5}), (2, 4, {'weight': 2}), (2, 5, {'weight': 3}), (3, 5, {'weight': 1}), (3, 8, {'weight': 6}), (4, 6, {'weight': 8}), (4, 7, {'weight': 7}), (4, 8, {'weight': 6}), (5, 7, {'weight': 2})]
```

Por ejemplo, la línea `1 4 5` representa una arista dirigida del vértice 1 al vértice 4 con peso 5.

**Diagrama (Caso G11 · Grafo dirigido con pesos · Ejemplo del README · 8 vértices · 9 aristas):**

Grafo dirigido con los vértices 1 a 8 y las siguientes aristas (origen → destino, peso entre paréntesis):

- 1 → 4 (5)
- 2 → 4 (2)
- 2 → 5 (3)
- 3 → 5 (1)
- 3 → 8 (6)
- 4 → 6 (8)
- 4 → 7 (7)
- 4 → 8 (6)
- 5 → 7 (2)

Disposición en tres columnas: a la izquierda los vértices 1, 2 y 3; en el centro el 4 y el 5; a la derecha el 6, el 7 y el 8.

## Tarea del alumno

Implementar en `solve.py` la siguiente función `build_digraph_with_weights`:

```python
def build_digraph_with_weights(edges_list, num_nodes, num_edges):
    ...
```

**Parámetros:**

- `edges_list`: lista de `num_edges` cadenas de texto, cada una con el formato `"origen destino peso"`. Por ejemplo: `['1 4 5', '2 4 2']`.
- `num_nodes`: entero con el número total de vértices.
- `num_edges`: entero con el número de aristas descritas en `edges_list`.

**Resultado:** un objeto `DiGraph` de **MiniGraph** (no una cadena de texto ni una lista con la salida) que contenga todos los **vértices** y las **aristas** con sus **pesos**.

**La función debe:**

- Crear todos los vértices desde 1 hasta `num_nodes`, incluidos los aislados, ya que crear los vértices únicamente al añadir aristas dejaría fuera los vértices aislados. Notar que son los identificadores de los vértices los que empiezan desde 1, no los índices de las listas de Python, que siguen empezando en 0.
- Convertir a enteros los tres valores de cada cadena de texto de `edges_list`.
- Incorporar cada arista en el sentido indicado, almacenando su peso con el atributo `weight`.

**Archivos principales:**

- `main.py`: lee la primera línea, obtiene los números de vértices y aristas, recoge las líneas de las aristas, llama a la función del alumno y formatea la salida.
- `solve.py`: contiene la lógica de construcción del grafo que debe implementar el alumno.
- `minigraph.py`: proporciona la implementación de grafos. No debe modificarse.
- `utils.py`: proporciona las funciones auxiliares de lectura. No debe modificarse.
- `vpl_evaluate.cases`: contiene las entradas y salidas esperadas de las pruebas.

## Pistas y consideraciones

- `split()` permite separar los tres valores de cada descripción de arista.
- Utilizar el módulo **MiniGraph** suministrado para gestión de grafos incluido en `minigraph.py` (no sustituirlo por **NetworkX** u otras bibliotecas externas).
- Los vértices se muestran mediante `graph.nodes()` y deben aparecer en orden de numeración.
- Las aristas se muestran mediante `graph.edges(data=True)`, con el orden que devuelve **MiniGraph**, donde cada elemento es una tupla con origen, destino y un diccionario que contiene el atributo `weight`.
