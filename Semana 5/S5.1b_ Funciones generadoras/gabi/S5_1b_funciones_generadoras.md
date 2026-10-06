# S5.1b: Funciones generadoras

- **Límite de entrega:** domingo, 18 de octubre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve_yield.py`, `utils.py`, `solve_iter.py` (número máximo de ficheros: 5)
- **Tipo de trabajo:** Individual

## Contexto

Este ejercicio corresponde a una secuencia de tres partes dedicada a resolver el problema de las N reinas mediante fuerza bruta:

1. Dado un número codificado en una determinada base de numeración, calcular el siguiente número.
2. Utilizando `yield`, programar un iterador de combinaciones para resolver problemas mediante fuerza bruta.
3. Utilizar ese iterador para calcular todas las soluciones que permiten colocar N reinas en un tablero de N × N.

Observaciones:

- Este enunciado corresponde a la **segunda parte** de la secuencia.
- Se reutiliza la función del primer ejercicio para generar todas las listas de dígitos de una longitud y base dadas.
- En este ejercicio todavía no se deben colocar reinas ni comprobar las reglas del tablero.

## Objetivo

Implementar un generador que produzca todas las combinaciones de `num_digits` dígitos en base `base`, en orden numérico creciente:

- Comenzar en `[0, ..., 0]`.
- Generar cada combinación una sola vez, manteniendo los ceros iniciales.
- Terminar después de producir `[base - 1, ..., base - 1]`.

Cada dígito de cualquiera de las combinaciones posibles puede tomar valores desde 0 hasta `base - 1` y en total se generan `base ** num_digits` combinaciones.

## Formato de entrada

Una única línea con dos números enteros separados por un espacio donde:

- `num_digits`: número de dígitos de cada combinación.
- `base`: base de numeración utilizada.

Por ejemplo, `4 2` indica que se deben generar todas las combinaciones de cuatro dígitos en base 2.

## Formato de salida

Imprimir una combinación por línea, con el formato de una lista de Python: corchetes y dígitos separados por coma y espacio.

- Las combinaciones deben aparecer en orden numérico creciente, con el dígito de la derecha cambiando más rápidamente.
- Todas las listas deben tener exactamente `num_digits` elementos.

**NOTA:** No se deben imprimir mensajes adicionales, como el número total de combinaciones.

## Ejemplo de caso de prueba

### Ejemplo 1: cuatro dígitos en base 2

**Entrada:**

```
4 2
```

**Salida esperada:**

```
[0, 0, 0, 0]
[0, 0, 0, 1]
[0, 0, 1, 0]
[0, 0, 1, 1]
[0, 1, 0, 0]
[0, 1, 0, 1]
[0, 1, 1, 0]
[0, 1, 1, 1]
[1, 0, 0, 0]
...
[1, 1, 1, 0]
[1, 1, 1, 1]
```

(Los puntos suspensivos `...` figuran así en el enunciado original; abarcan las combinaciones intermedias hasta `[1, 1, 1, 0]`.)

### Ejemplo 2: dos dígitos en base 3

**Entrada:**

```
2 3
```

**Salida esperada:**

```
[0, 0]
[0, 1]
[0, 2]
[1, 0]
[1, 1]
[1, 2]
[2, 0]
[2, 1]
[2, 2]
```

**Diagrama (Caso 02 · G22):** entrada `2 3`, 2 dígitos, base 3, 9 combinaciones. La salida se lee de izquierda a derecha y de arriba abajo, en una cuadrícula de 3 × 3 con la secuencia generada en orden creciente:

| 01 `[0, 0]` (inicio) | 02 `[0, 1]` | 03 `[0, 2]` |
|---|---|---|
| **04 `[1, 0]`** | **05 `[1, 1]`** | **06 `[1, 2]`** |
| **07 `[2, 0]`** | **08 `[2, 1]`** | **09 `[2, 2]`** (final) |

Inicio `[0, 0]`, final `[2, 2]`. El dígito derecho cambia primero; al agotarse la base, se propaga el acarreo.

## Tarea del alumno

Reutilizar la función `next_number(digits, base)` de la primera parte del ejercicio y completar la clase `My_Iterator` para generar las combinaciones mediante `yield`:

```python
def next_number(digits, base):
    ...

class My_Iterator:
    def __init__(self, num_digits, base):
        ...

    def next(self):
        ...
```

La función debe:

- Reutilizar `next_number(digits, base)` para obtener la **siguiente lista de dígitos** en la base indicada.
- Guardar en el **constructor** el número de dígitos y la base.
- Implementar `next()` como una **función generadora** que entregue cada combinación mediante `yield`.
- Incluir tanto la combinación inicial como la final y detenerse al terminar la enumeración.
- Devolver las listas de dígitos, ya que la impresión de esas listas la realiza `main.py`.

Para usar esta implementación desde `main.py`:

```python
obj = My_Iterator(num_digits, base)
for c in obj.next():
    print(c)
```

Archivos principales:

- `main.py`: lee el número de dígitos y la base, crea un objeto `My_Iterator`, recorre el generador e imprime cada combinación. Actualmente utiliza la implementación de `solve_yield.py`.
- `solve_yield.py`: contiene la implementación con `yield`, correspondiente al enfoque solicitado en el enunciado.
- `solve_iter.py`: contiene una implementación alternativa con el protocolo de iteración de Python (`__iter__()` y `__next__()`), útil para comparar ambos enfoques.
- `utils.py`: proporciona las funciones auxiliares de entrada utilizadas por `main.py`.
- `vpl_evaluate.cases`: contiene los casos de prueba locales.

## Estrategia requerida

Utilizar `yield` para generar las combinaciones de forma sucesiva, sin construir previamente una lista con todas ellas:

1. Crear la combinación inicial con todos sus dígitos a cero.
2. Emitir esa combinación mediante `yield`.
3. Mientras no se haya alcanzado la combinación con todos los dígitos iguales a `base - 1`, calcular el siguiente número con `next_number` y emitirlo.
4. Terminar la función generadora después de emitir la última combinación.

**NOTA:** Este recorrido enumera exhaustivamente todas las posibles combinaciones y sirve como base para una búsqueda por fuerza bruta. En esta parte del ejercicio en concreto no se filtran combinaciones ni se aplica poda.

## Pistas y consideraciones

- La suma de una unidad comienza por el dígito de la derecha y propaga el acarreo hacia la izquierda cuando sea necesario.
- Conserva la longitud de las listas y los ceros iniciales.
- Evita modificar una lista ya emitida al calcular la siguiente; trabajar con una copia permite conservar los valores anteriores.
- Detecta correctamente la última combinación para no volver a empezar por `[0, ..., 0]` y generar un bucle infinito.
- En una función generadora basta con retornar o alcanzar el final para terminar la iteración; no es necesario lanzar `StopIteration` explícitamente.

**NOTA:** Las dos implementaciones de esta parte del ejercicio se utilizan de forma distinta: con `solve_yield.py` se recorre `obj.next()`, mientras que con `solve_iter.py` se recorre directamente `obj`. Para probar la alternativa, cambia tanto la importación como el bucle en `main.py`, dejando activa solo una versión.
