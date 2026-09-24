# S3b: Manhattan Distance

**Límite de entrega:** domingo, 4 de octubre de 2026, 23:59
**Ficheros requeridos:** main.py, solve.py, utils.py
**Número máximo de ficheros:** 4
**Tipo de trabajo:** Individual

## Contexto

Estamos situados en una intersección de un tablero de tamaño infinito, orientados inicialmente hacia el Norte. Nos movemos siguiendo una secuencia de instrucciones, cada una de las cuales indica un giro de 90 grados hacia la izquierda (L) o hacia la derecha (R), seguido del número de cuadrículas que debemos avanzar.

La distancia de Manhattan entre dos posiciones es la suma de las diferencias absolutas de sus coordenadas. Así, representando la posición inicial como (0, 0) y la final como (x, y), esta distancia es:

```
distancia = |x| + |y|
```

> **NOTA:** Esta medida indica la distancia mínima entre ambas posiciones al desplazarse únicamente en horizontal y vertical, no la longitud total del recorrido realizado.

## Objetivo

Escribir la lógica de un programa en Python que ejecute, en orden, todas las instrucciones de movimiento y calcule la distancia de Manhattan entre la posición inicial y la posición final.

Se parte de (0, 0) mirando hacia el Norte. En cada instrucción se debe girar primero y avanzar después.

## Formato de entrada

La entrada de datos tiene el siguiente formato:

```
N
instruccion1
instruccion2
... instruccionN
```

donde:

- La primera línea contiene un entero **N** que indica el número de instrucciones.
- Las siguientes N líneas contienen una instrucción cada una, sin espacios entre la letra y el número:
  - `L<numero>`: girar 90 grados a la izquierda y avanzar el número indicado de cuadrículas.
  - `R<numero>`: girar 90 grados a la derecha y avanzar el número indicado de cuadrículas.

**Consideraciones:**

- Los giros son relativos a la orientación actual, no a la orientación inicial.
- El número de cuadrículas puede tener varias cifras; por ejemplo, `L953`.

## Formato de salida

Se debe imprimir una única línea con un entero: la distancia de Manhattan entre la posición inicial y la posición final.

No se deben añadir etiquetas, mensajes explicativos ni las coordenadas finales.

## Ejemplo de caso de prueba

### Ejemplo 1

**Entrada:**

```
2
R2
L3
```

**Salida esperada:**

```
5
```

Tras girar a la derecha se avanzan dos cuadrículas hacia el Este; después, al girar a la izquierda, se avanzan tres hacia el Norte. La posición final es (2, 3) y la distancia es |2| + |3| = 5.

### Ejemplo 2

**Entrada:**

```
3
R3
R3
R2
```

**Salida esperada:**

```
4
```

La posición final es (1, -3). La distancia es |1| + |-3| = 4, aunque se hayan recorrido ocho cuadrículas.

### Ejemplo 3

**Entrada:**

```
4
R5
L5
R5
R3
```

**Salida esperada:**

```
12
```

La posición final es (10, 2) y la distancia es |10| + |2| = 12.

*(El enunciado incluye una figura "c03 | Distancia de Manhattan" que detalla, para este Ejemplo 3, la traza paso a paso: partiendo de (0,0) mirando al Norte, el paso 1 (R5) gira hacia el Este y avanza a (5,0); el paso 2 (L5) gira hacia el Norte y avanza a (5,5); el paso 3 (R5) gira hacia el Este y avanza a (10,5); el paso 4 (R3) gira hacia el Sur y avanza a (10,2). La posición final es (10,2), con distancia de Manhattan |10|+|2| = 12, y un total de 18 cuadrículas recorridas en el trayecto (aclarando que esa cifra de pasos recorridos no es lo que se devuelve).)*

## Tarea del alumno

Implementar la siguiente función en `solve.py`:

```python
def solve(items):
    ...
```

**Parámetro:** `items`, una lista de cadenas con las instrucciones en orden, por ejemplo, `['R2', 'L3']`. La primera línea de la entrada, que contiene N, no forma parte de esta lista.

**Retorno:** un entero con la distancia de Manhattan desde el origen hasta la posición final.

La función debe:

- Mantener la posición y la orientación actuales durante todo el recorrido.
- Interpretar cada instrucción, aplicar el giro y avanzar las cuadrículas indicadas.
- Devolver la distancia final como un entero, no como una cadena ni como una tupla de coordenadas.
- No leer de la entrada estándar ni imprimir desde `solve`; esas tareas corresponden a `main.py`.

### Archivos principales

- **main.py**: lee el número de instrucciones y las líneas de entrada, construye una lista de cadenas, llama a `solve(input_list)` e imprime el entero devuelto.
- **solve.py**: contiene la función que calcula y devuelve la distancia de Manhattan.
- **tuple_tools.py**: proporciona `int_tuple_add` e `int_tuple_multiply` para sumar tuplas componente a componente y multiplicarlas por un entero, respectivamente.
- **vpl_evaluate.cases**: contiene los casos de prueba y las salidas esperadas.

### Estrategia requerida

Procesar las instrucciones secuencialmente, conservando únicamente la posición y la orientación actuales:

1. Inicializar la posición en (0, 0) y la orientación hacia el Norte.
2. Para cada instrucción, identificar el sentido del giro y el número de cuadrículas.
3. Actualizar la orientación mediante un giro de 90 grados.
4. Actualizar las coordenadas según la nueva orientación y la distancia indicada.
5. Calcular y devolver `abs(x) + abs(y)` al terminar todas las instrucciones.

### Pistas y consideraciones

- Un giro cambia la orientación, pero no la posición; el avance se realiza después del giro.
- El orden circular Norte, Este, Sur y Oeste puede facilitar la gestión de los giros.
- No supongas que el número de pasos tiene una sola cifra: utiliza toda la parte numérica de la instrucción.
- Las coordenadas pueden ser negativas. Aplica el valor absoluto a cada coordenada al calcular la distancia final.
- No sumes las longitudes de todos los movimientos: se pide la distancia entre los extremos del recorrido.
