# S8.1a Branch and Bound (clase Node)

- **Límite de entrega:** domingo, 15 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `node.py`, `utils.py`
- **Número máximo de ficheros:** 4
- **Tipo de trabajo:** Individual

## Contexto

Este ejercicio es la **primera parte (de una serie de 2)** sobre **Branch & Bound** aplicado al problema de la **Mochila 0/1**.

## Objetivo

El objetivo de esta primera parte es **declarar la clase `Node`** que se utilizará para programar el **recorrido en profundidad** en las siguientes partes, y **comprobar su funcionamiento** creando manualmente algunos **nodos** del árbol de decisión y mostrando sus atributos (`index`, `room`, `taken`, `value`) junto con la **estimación** (`estimate`) calculada a partir de los **ítems** restantes.

## Formato de entrada

La entrada seguirá el siguiente formato:

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

**Ejemplo (3 ítems, capacidad 10):**

```
3 10
45 5
48 8
35 3
```

Interpretación:

- Ítem 0: valor 45, peso 5.
- Ítem 1: valor 48, peso 8.
- Ítem 2: valor 35, peso 3.

## Formato de salida

La salida mostrará la información de los **nodos del árbol de decisión** (tres en este caso), una línea por nodo, con el siguiente formato:

```
Node 1: <index> <room> <taken> <value> <estimate>
Node 2: <index> <room> <taken> <value> <estimate>
Node 3: <index> <room> <taken> <value> <estimate>
```

donde:

- `index`: **nivel del nodo** en el árbol (**índice** del siguiente ítem a considerar).
- `room`: **capacidad** restante en la mochila.
- `taken`: **lista de índices** (*0-based*) de los ítems tomados hasta ese nodo.
- `value`: **valor** acumulado de los ítems tomados.
- `estimate`: **estimación** optimista del valor máximo alcanzable desde ese nodo (`value + <suma_valores_items_restantes>`).

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
Node 1: 1 10 [] 0 83
Node 2: 2 2 [1] 48 83
Node 3: 3 7 [2] 35 35
```

Interpretación de cada nodo:

- **Node 1**: no se ha tomado ningún ítem. `index=1` (siguiente ítem a considerar es el 1), `room=10` (capacidad intacta), `taken=[]`, `value=0`, `estimate=0+48+35=83`.
- **Node 2**: se ha tomado el ítem 1 (valor 48, peso 8). `index=2`, `room=10-8=2`, `taken=[1]`, `value=48`, `estimate=48+35=83`.
- **Node 3**: se ha tomado el ítem 2 (valor 35, peso 3). `index=3` (no quedan ítems restantes), `room=10-3=7`, `taken=[2]`, `value=35`, `estimate=35+0=35`.

## Tarea del alumno

Implementar la clase `Node` en `node.py`:

```python
class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room  = room

    def estimate(self, items):
        return self.value + sum(item.value for item in items[self.index:])
```

El método `estimate(items)` calcula una **cota superior** del valor alcanzable desde el nodo actual: suma el valor acumulado (`self.value`) más el valor de todos los ítems desde `self.index` hasta el final.

> **NOTA:** Esta estimación se utilizará en la última parte del ejercicio para la **poda** del árbol de búsqueda.
