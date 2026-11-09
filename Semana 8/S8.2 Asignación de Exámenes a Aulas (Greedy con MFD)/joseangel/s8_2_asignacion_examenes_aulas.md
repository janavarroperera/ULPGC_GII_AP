# S8.2 Asignación de Exámenes a Aulas

- **Límite de entrega:** domingo, 15 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `utils.py`
- **Número máximo de ficheros:** 4
- **Tipo de trabajo:** Individual

## Contexto

En este ejercicio se pide implementar una estrategia **Greedy** para asignar exámenes (con necesidades de capacidad conocidas) a aulas (con capacidades conocidas) aplicando el algoritmo conocido como **Max-Fit Decreasing (MFD)**.

Esta estrategia consiste en ordenar los exámenes de mayor a menor y asignar cada uno al aula con una capacidad mayor disponible (primera aula en la que "quepa", priorizando las "grandes", según las necesidades del examen).

## Objetivo

Implementar la estrategia Greedy MFD para asignar cada examen a un aula, devolviendo el número de aulas usadas, el desperdicio total de capacidad y la capacidad del aula asignada a cada examen (en el orden de entrada), o indicando que la asignación no es posible.

## Formato de entrada

```
n m
e1 e2 ... en
c1 c2 ... cm
```

donde:

- `n`: número de exámenes
- `m`: número de aulas
- `e1..en`: tamaño en alumnos (necesidades) de cada examen
- `c1..cm`: capacidades (máximas) de cada aula

## Formato de salida

Si la asignación es posible (es decir, todos los exámenes caben):

```
rooms_used=<k> waste=<w>
assign=[cap1, cap2, ...]
```

donde:

- `rooms_used` es el número de exámenes asignados (debe coincidir con `n` si es posible la asignación).
- `waste = sum(assign) − sum(exams)` es el "desperdicio" total de capacidad (suma de las diferencias entre las capacidades asignadas y las necesidades de los exámenes), proporcionado solo a nivel informativo.
- `assign[i]` es la capacidad del aula asignada al examen `exams[i]` (con mismo orden de entrada).

Si la asignación no es posible (si algún examen no cabe en ninguna aula disponible):

```
ERROR
```

## Ejemplo de caso de prueba

**Entrada:**

```
4 5
70 45 30 10
80 50 40 30 10
```

**Salida:**

```
rooms_used=4 waste=45
assign=[80, 50, 40, 30]
```

### Diagrama del caso (`c02_feasible — Factible`)

El diagrama muestra a la izquierda los **exámenes** (necesidad) y a la derecha las **aulas** (capacidad), unidos por flechas de asignación etiquetadas con el desperdicio (`+waste`):

| Examen (necesidad) | → | Aula (capacidad) | Desperdicio |
|---|---|---|---|
| E1 (70) | → | A1 (80) | +10 |
| E2 (45) | → | A2 (50) | +5 |
| E3 (30) | → | A3 (40) | +10 |
| E4 (10) | → | A4 (30) | +20 |

- El aula **A5 (10)** queda **sin usar**.
- Desperdicio total: 10 + 5 + 10 + 20 = 45.
- Resultado mostrado al pie del diagrama: `rooms_used=4 waste=45 assign=[80, 50, 40, 30]`.
- Leyenda: azul = Examen (necesidad); verde = Aula usada; gris = Aula sin usar; naranja = Asignación (+waste).

## Tarea del alumno

Implementa la siguiente función en `solve.py`:

```python
def solve_mfd_feasible(exams, rooms):
    """
    Asigna exámenes a aulas usando Max-Fit Decreasing (MFD).

    Args:
        exams: lista de necesidades de alumnos por examen
        rooms: lista de capacidades de aulas

    Returns:
        tuple: (rooms_used, waste, assign_cap) o (None, None, None) si no es posible
    """
```

> **NOTA:** El fichero `main.py` lee y parsea la entrada de datos para obtener `n`, `m`, `exams` y `rooms`, llama a la implementación del algoritmo **MFD** de `solve.py` y formatea la salida para verificar que es la esperada según los casos de prueba.

### Estrategia Greedy: Max-Fit Decreasing (MFD)

1. Ordena los exámenes de **mayor a menor** y las aulas de **mayor a menor**.
2. Recorre los exámenes (en ese orden) y asigna a cada uno la **primera aula**, por ese orden, que tenga **capacidad suficiente**, teniendo en cuenta que, una vez usada, esa aula no puede reutilizarse.
3. Si en algún momento no hay aula que soporte el examen actual, la solución para este caso es imposible y debe devolverse `None` para que `main.py` muestre entonces `ERROR`.
4. Si se logran asignar todos los exámenes, calcula `rooms_used`, `waste` y construye `assign` en el orden original de `exams`.
