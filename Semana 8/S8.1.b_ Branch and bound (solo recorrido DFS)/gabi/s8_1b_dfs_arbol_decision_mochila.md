# S8.1.b Branch and Bound (solo recorrido DFS)

- **Límite de entrega:** domingo, 15 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `node.py`, `utils.py`
- **Tipo de trabajo:** Individual

## Contexto

Este ejercicio es la **segunda parte (de una serie de 3)** sobre el problema de la **Mochila 0/1**. La primera parte consistió en declarar la clase `Node` (en `node.py`) mientras que en esta segunda parte se pide programar, utilizando dicha clase, el **recorrido en profundidad (DFS)** completo del árbol de decisión asociado a la mochila, donde cada nivel del árbol corresponde a un ítem y desde cada nodo se generan dos hijos ("tomar" o "no tomar" el ítem).

## Objetivo

- Programar el recorrido en profundidad (DFS) del árbol de decisión de la Mochila 0/1.
- Devolver el orden de visita de los nodos (lista de sus `index`).
- En esta parte **no se optimiza ni se aplica poda ni bound**, solo se recorre el árbol completo.

## Formato de entrada

```
N C
v1 w1
v2 w2
...
vN wN
```

donde:

- `N` es el número de ítems.
- `C` es la capacidad máxima de la mochila.
- Cada línea posterior contiene dos enteros: `vi` (valor del ítem i) y `wi` (peso del ítem i).

Ejemplo (3 ítems, capacidad 10):

```
3 10
45 5
48 8
35 3
```

> **NOTA:** en esta parte los parámetros `taken`, `value` y `room` del nodo no se utilizan y el único valor relevante es `index`, que indica el ítem que corresponde procesar en ese nivel. Los nodos del árbol se indexan desde 0 (raíz, antes del primer ítem) hasta N (hojas, cuando ya se han considerado todos los ítems).

## Formato de salida

El programa imprime una única línea con la **lista de índices** de los nodos visitados en el **recorrido DFS** completo, en formato de lista de Python.

```
[0, 1, 2, 3, 3, 2, 3, 3, 1, 2, 3, 3, 2, 3, 3]
```

## Ejemplo de caso de prueba

**Entrada:**

```
3 10
45 5
48 8
35 3
```

**Salida esperada:**

```
[0, 1, 2, 3, 3, 2, 3, 3, 1, 2, 3, 3, 2, 3, 3]
```

El árbol tiene 3 niveles de ítems (índices 0, 1, 2) y las **hojas** tienen `index = 3`. El recorrido DFS completo visita los **15 nodos** del árbol en el orden mostrado.

### Diagrama (`Case_1 - Árbol de decisión (DFS) - 3 items, 15 nodos`)

Cada nodo se muestra como `idx` (índice del nodo) y `#V` (número de orden de visita). Las aristas están etiquetadas con **T** (tomar) y **N** (no tomar). Leyenda: naranja = nodo interno, azul = raíz, verde = hoja.

```
idx 0 (#1)  raíz
├─ T → idx 1 (#2)
│   ├─ T → idx 2 (#3)
│   │   ├─ T → idx 3 (#4)   hoja
│   │   └─ N → idx 3 (#5)   hoja
│   └─ N → idx 2 (#6)
│       ├─ T → idx 3 (#7)   hoja
│       └─ N → idx 3 (#8)   hoja
└─ N → idx 1 (#9)
    ├─ T → idx 2 (#10)
    │   ├─ T → idx 3 (#11)  hoja
    │   └─ N → idx 3 (#12)  hoja
    └─ N → idx 2 (#13)
        ├─ T → idx 3 (#14)  hoja
        └─ N → idx 3 (#15)  hoja
```

Leyendo los `idx` en orden de visita (#1 a #15) se obtiene la salida esperada.

## Tarea del alumno

Implementar la siguiente función en `solve.py` que realiza el **recorrido DFS del árbol de decisión** y devuelve el **orden de visita** de los nodos:

```python
def solve_branch_and_bound_DFS(capacity, items, record_visiting_order=False):
    """
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora solo devuelve la lista de nodos visitados
    """
```

La función debe:

- Crear el nodo raíz con `index = 0` (y `taken = []`, `value = 0`, `room = 0`).
- Usar la lista `alive` como **pila de nodos vivos** para programar el **recorrido DFS**.
- Registrar en `visiting_order` el `index` de cada **nodo visitado** (cuando `record_visiting_order=True`).
- Ramificar primero por la derecha y luego por la izquierda (haciendo `push` en la pila) de forma que, al hacer `pop`, **se procese primero la rama izquierda**.
- Detener la expansión cuando `index >= len(items)` (**hojas del árbol**).
- Devolver `"0, [], visiting_order"` (teniendo en cuenta que, en esta parte del ejercicio, el valor óptimo y `taken` no se calculan).

### Consideraciones

- `node.py`: define la clase `Node` (con `index`, `taken`, `value`, `room` y el método `estimate`).
- `main.py` se encarga de leer la entrada, construir la lista de ítems, llamar a la función de `solve.py` y formatear la salida.
