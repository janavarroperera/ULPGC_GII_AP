# S11.3: Mochila 0/1 (Programación Dinámica)

> **Límite de entrega:** domingo, 6 de diciembre de 2026, 23:59
> **Ficheros requeridos:** `main.py`, `solve.py`, `utils.py`
> **Número máximo de ficheros:** 4
> **Tipo de trabajo:** Individual

## Contexto

Se dispone de `N` objetos y de una mochila con una capacidad máxima de peso. Cada objeto tiene un valor (beneficio) y un peso. Cada objeto puede seleccionarse una sola vez o no seleccionarse: no se permite fraccionarlo ni introducir varias copias, y no es obligatorio llenar exactamente la mochila.

Este problema se puede resolver mediante las dos técnicas de Programación Dinámica: **Tabulation** y **Memoization**.

## Objetivo

Elegir qué objetos introducir en la mochila para **maximizar el beneficio total sin superar su capacidad**. Además de calcular el beneficio máximo, hay que reconstruir la lista `taken` con los índices de los objetos elegidos (sin repeticiones y en orden creciente).

Consideraciones:

- Implementar la recurrencia mediante una **tabla iterativa** y mediante **recursión con un diccionario** de resultados calculados.
- Ambas versiones deben devolver el **mismo beneficio y la misma selección**, aplicando el **mismo criterio de desempate**.

## Formato de entrada

```
N capacity
value1 weight1
value2 weight2
...
valueN weightN
```

donde:

- La primera línea contiene dos enteros: el número de objetos `N` y la capacidad máxima `capacity`.
- Las siguientes `N` líneas contienen dos enteros cada una: primero el **valor** del objeto y después su **peso**.
- Los objetos se numeran del 1 al `N`, según su orden de aparición.

## Formato de salida

Una única línea:

```
beneficio_maximo [indice1, indice2, ...]
```

donde `taken` (`[indice1, indice2, ...]`) es una **lista de índices** (no una lista de ceros y unos como cuando se usa como máscara de bits). Si no se selecciona ningún objeto, la solución es `0 []`.

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
80 [1, 3]
```

Los objetos `1` y `3` pesan `5 + 3 = 8`, sin superar la capacidad `10`, y aportan un beneficio total de `45 + 35 = 80`.

### Diagrama explicativo (Knapsack03_EjemploPDF)

Mochila 0/1, 3 objetos, capacidad 10.

| Beneficio máximo | Peso utilizado | Capacidad libre | Objetos elegidos |
|:---:|:---:|:---:|:---:|
| 80 | 8 / 10 | 2 | 2 / 3 |

**Tabla original de objetos + solución** (se conserva el orden de entrada; los objetos "TOMAR" pertenecen a la mochila óptima):

| Índice | Valor | Peso | Decisión |
|:---:|:---:|:---:|:---:|
| 1 | 45 | 5 | **TOMAR** |
| 2 | 48 | 8 | Descartar |
| 3 | 35 | 3 | **TOMAR** |

**Ocupación de la mochila:** 8 de 10 unidades de peso (80,00 %).
Peso total: 8 ≤ 10 | Beneficio total: 80 | Sin repetir objetos.

**Salida esperada:** `80 [1, 3]`

**Criterio de desempate:** si tomar y descartar dan el mismo beneficio, se descarta el objeto actual.

## Tarea del alumno

Implementar las siguientes funciones en `solve.py`:

```python
def solve_tabulation(items, capacity):
    ...

def solve_memoization(items, capacity):
    ...
```

donde ambas funciones reciben:

- `items`: una lista de objetos `Item(index, value, weight)` (en orden de entrada), donde `Item` es una `namedtuple` ya definida y sus campos se consultan con `.index`, `.value` y `.weight`.
- `capacity`: la capacidad máxima de la mochila, como un valor entero.

Ambas funciones devuelven una tupla `(beneficio_maximo, taken)`, formada por un valor entero con el beneficio máximo alcanzable y una lista de índices de los objetos seleccionados.

Consideraciones:

1. Implementar el cálculo del beneficio mediante **tabulation** y reconstruir `taken` a partir de la tabla.
2. Implementar el cálculo mediante **memoization** y reconstruir `taken` a partir de los valores guardados en el diccionario. El diccionario debe gestionarse manualmente: **no puede sustituirse por decoradores de `functools`**, como `cache` o `lru_cache`.
