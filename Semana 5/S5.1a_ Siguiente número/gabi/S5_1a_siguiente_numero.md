# S5.1a: Siguiente número

- **Límite de entrega:** domingo, 18 de octubre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `utils.py` (número máximo de ficheros: 4)
- **Tipo de trabajo:** Individual

## Contexto

Este ejercicio es el primero de tres partes dedicadas a resolver el problema de las N reinas mediante fuerza bruta:

1. Calcular el siguiente número a partir de un número codificado en una determinada base de numeración.
2. Programar un iterador de combinaciones con `yield` para resolver problemas mediante fuerza bruta.
3. Utilizar ese iterador para calcular todas las soluciones para colocar N reinas en un tablero de ajedrez de N × N.

**NOTA:** Este ejercicio en concreto solo aborda la primera parte.

## Objetivo

Dado un número codificado en una determinada base de numeración, calcular el siguiente número.

El número se representa mediante una lista de dígitos, ordenados de mayor a menor peso. El resultado debe conservar la misma cantidad de dígitos que la entrada. Si al sumar 1 se necesita un dígito adicional a la izquierda, ese dígito se elimina para mantener la longitud original de la lista. Por eso, al sumar 1 al número más grande que cabe en la lista, todos sus dígitos pasan a ser cero.

Por ejemplo, en base 10, con tres dígitos:

```
998 + 1 → 999
999 + 1 → 000
```

**NOTA:** Vemos que el siguiente número es 999 (no 1000) porque solo hay tres posiciones.

En base 2 ocurre igual, pero el dígito máximo es 1:

```
[1, 1, 0] + 1 → [1, 1, 1]
[1, 1, 1] + 1 → [0, 0, 0]
```

Ejemplos:

| Número de entrada | Base | Siguiente número |
|---|---|---|
| 1357 | 10 | 1358 |
| 0101 | 2 | 0110 |
| 02333 | 4 | 03000 |
| 011111111 | 2 | 100000000 |
| 111111111 | 2 | 000000000 |

## Formato de entrada

La primera línea contiene dos enteros separados por un espacio:

- `N`: cantidad de números que hay que procesar.
- `B`: base de numeración, común a todos ellos.

Las siguientes `N` líneas contienen un número cada una, escrito como una secuencia de dígitos sin espacios.

```
N B
numero1
numero2
...
numeroN
```

Observaciones:

- Cada dígito debe cumplir `0 <= dígito < B`.
- Los números pueden tener distintas longitudes y contener ceros a la izquierda; debe conservarse la longitud de cada uno.
- El formato proporcionado admite bases de 2 a 10 y no contempla letras para representar dígitos de bases mayores.
- La lógica incluida en `main.py` ya se encarga de convertir cada carácter en un entero.

## Formato de salida

Por cada número de entrada se imprime una línea con dos listas de enteros separadas por un guion (con un espacio a cada lado). Las listas se muestran con el formato habitual de Python: corchetes y elementos separados por coma y espacio.

```
[0, 1, 0, 1] - [0, 1, 1, 0]
```

## Ejemplo de caso de prueba

Ejemplo del enunciado: siete números en base 2.

**Entrada:**

```
7 2
00
01
10
11
011
101
0111
```

**Salida esperada:**

```
[0, 0] - [0, 1]
[0, 1] - [1, 0]
[1, 0] - [1, 1]
[1, 1] - [0, 0]
[0, 1, 1] - [1, 0, 0]
[1, 0, 1] - [1, 1, 0]
[0, 1, 1, 1] - [1, 0, 0, 0]
```

**Casos de prueba · Base 2** (10 números · sumar 1 conservando el número de dígitos; fuente: `vpl_evaluate.cases`, cada fila muestra el número de entrada y la línea exacta esperada):

| Entrada | Salida esperada |
|---|---|
| 00 | [0, 0] - [0, 1] |
| 01 | [0, 1] - [1, 0] |
| 10 | [1, 0] - [1, 1] |
| 11 | [1, 1] - [0, 0] |
| 011 | [0, 1, 1] - [1, 0, 0] |
| 101 | [1, 0, 1] - [1, 1, 0] |
| 0111 | [0, 1, 1, 1] - [1, 0, 0, 0] |
| 01011 | [0, 1, 0, 1, 1] - [0, 1, 1, 0, 0] |
| 01010101111 | [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1] - [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0] |
| 01111111111 | [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] - [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |

## Tarea del alumno

Implementar la función `next_number()` en `solve.py`.

```python
def next_number(digits, base):
    ...
```

donde:

- `digits`: lista de enteros que representa el número donde el **dígito de mayor peso** está en la **posición inicial**.
- `base`: **base de numeración** del número.

La función debe retornar una nueva lista con los **dígitos del siguiente número**, de la misma longitud que `digits`.

La función debe:

- Sumar una unidad en la base indicada, **propagando los acarreos necesarios**.
- Mantener el ancho fijo de la representación, sin añadir dígitos al resultado.
- Trabajar sobre una copia para no modificar la lista de entrada, de acuerdo con la estructura proporcionada en `solve.py`.
- Devolver el resultado, sin leer datos ni imprimir dentro de la función; esas tareas ya las gestiona `main.py`.

## Estrategia requerida

El comportamiento requerido es el incremento en una base dada con un número fijo de dígitos y un enfoque válido es la suma con acarreo sobre la lista:

1. Trabajar sobre una copia de los dígitos.
2. Comenzar por el último dígito, que es el de menor peso.
3. Incrementarlo en una unidad. Si alcanza el valor de la base, convertirlo en cero y propagar el acarreo hacia la izquierda.
4. Detener el recorrido cuando no quede acarreo o se hayan procesado todos los dígitos.
5. Devolver la lista sin añadir una posición para un posible acarreo final.

**NOTA:** En este VPL no es necesario implementar `yield` ni resolver el problema de las **N reinas**.

## Pistas y consideraciones

- No supongas siempre que es **base 2**: el valor máximo de un dígito es `base - 1`.
- Conserva los ceros a la izquierda que correspondan al resultado; no elimines posiciones de la lista.
- Comprueba los casos sin acarreo, con varios acarreos consecutivos y con desbordamiento total.
- Por ejemplo, en base 4, `02333` pasa a `03000`, mientras que `33` pasa a `00`.
- Para una lista de longitud L, el resultado representa (valor + 1) módulo B^L.
