# S11.2: Ladrón de casas (Programación Dinámica)

> **Límite de entrega:** domingo, 6 de diciembre de 2026, 23:59
> **Ficheros requeridos:** `main.py`, `solve.py`, `utils.py`
> **Número máximo de ficheros:** 4
> **Tipo de trabajo:** Individual

## Contexto

Un ladrón quiere robar en una fila de casas. Cada casa contiene un valor conocido que podría robar. Debe elegir qué casas robar para conseguir el **mayor beneficio posible**, pero cumpliendo que **no puede robar en dos casas consecutivas**.

Se resuelve mediante **Programación Dinámica con Tabulation**, recuperando los números (índices) de las casas elegidas. Las casas se numeran desde `1` en el orden en que aparecen en la entrada. La fila de casas es lineal (**problema 1-D**): la primera y la última casa no son vecinas entre sí, salvo cuando solo hay dos casas.

## Objetivo

- Calcular el máximo beneficio que puede obtenerse **sin seleccionar casas consecutivas**.
- Reconstruir el recorrido para determinar qué casas seleccionar para alcanzar ese beneficio.
- Devolver el **beneficio** y una lista de números de casa (**índices**) en orden creciente.

Para cada casa se consideran dos posibilidades:

- **Robarla:** sumar su valor al mejor beneficio obtenido hasta dos posiciones antes.
- **No robarla:** conservar el mejor beneficio obtenido hasta la posición anterior.

La **ecuación de recurrencia**, expresada con índices internos desde `0`, es:

```
t(j) = 0                              si j < 0
t(j) = max(t(j - 2) + items[j], t(j - 1))   si j >= 0
```

## Formato de entrada

1. La primera línea contiene un entero `N` (con `N >= 2`), el **número de casas**.
2. Las siguientes `N` líneas contienen, cada una, un entero con el **valor de cada casa**.

```
N
v1
v2
...
vN
```

> **NOTA:** `main.py` lee estos datos y construye la lista `items`, donde `items[0]` es el valor de la casa 1.

## Formato de salida

Se imprimen exactamente dos líneas:

1. El **beneficio máximo**, como un entero sin etiquetas.
2. La **lista de casas elegidas** (índices comenzando en `1`, en orden creciente), con el formato habitual de una lista de Python: corchetes y elementos separados por coma y espacio.

## Ejemplo de caso de prueba

**Entrada:**

```
5
3
10
3
1
2
```

**Salida esperada:**

```
12
[2, 5]
```

La casa `2` aporta `10` y la casa `5` aporta `2`. No son consecutivas y el beneficio total es `12`.

Para este caso, la tabla de beneficios sería `[3, 10, 10, 11, 12]`.

### Diagrama explicativo (Case3, "El problema del ladrón")

Tabulation y reconstrucción, 5 casas, numeración desde 1.

**1. Valores originales y solución sobre la fila de casas**

| Casa 1 | Casa 2 | Casa 3 | Casa 4 | Casa 5 |
|:---:|:---:|:---:|:---:|:---:|
| 3 | 10 | 3 | 1 | 2 |
| No elegida | **ELEGIDA** | No elegida | No elegida | **ELEGIDA** |

**2. Tabla original de valores y beneficios óptimos por prefijo**

| Casa (j + 1) | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Valor original: `items[j]` | 3 | 10 | 3 | 1 | 2 |
| Máximo del prefijo: `table[j]` | 3 | 10 | 10 | 11 | 12 |
| Solución final | No | Sí | No | No | Sí |

Prefijo: desde la casa 1 hasta cada columna. Índices internos `j`: 0 a 4.

**3. Solución y salida esperada**

Beneficio = 10 + 2 = 12. Salida:

```
12
[2, 5]
```

Verificación: casas no consecutivas; suma de valores = beneficio máximo.

## Tarea del alumno

Implementar la siguiente función en `solve.py`:

```python
def solve_tabulation(items):
```

donde `items` es una lista de `N` enteros no negativos con los valores de las casas en su orden original.

La función debe retornar una tupla `(max_benefit, taken)`, donde `max_benefit` es un entero con el máximo beneficio y `taken` es una lista de enteros con los números de las casas elegidas, desde 1 y en orden creciente.

> **NOTA:** Resolver el problema de forma iterativa mediante una **tabla de programación dinámica**, completando primero el cálculo del beneficio y después la reconstrucción de las casas elegidas.
