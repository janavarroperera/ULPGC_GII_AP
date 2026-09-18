# S1a: Manejo de arrays

**Límite de entrega:** domingo, 20 de septiembre de 2026, 23:59
**Ficheros requeridos:** `main.py`, `solve.py`, `utils.py`
**Tipo de trabajo:** Individual

---

## Contexto

En los algoritmos genéticos es habitual trabajar con soluciones representadas como listas o permutaciones. Una operación frecuente es el cruce entre dos soluciones padre para generar una nueva solución hija.

En este ejercicio se trabaja con dos listas llamadas `padre` y `madre`. Ambas contienen los mismos elementos, pero posiblemente en distinto orden. El objetivo es aplicar un operador de cruce llamado **cruce de orden** (**Order Crossover**).

El cruce de orden toma un segmento de la lista padre y completa el resto de posiciones usando los elementos de la lista madre, respetando su orden relativo y evitando repetir elementos.

## Objetivo

Implementar una función que, dadas dos listas y dos puntos de corte, genere una nueva lista hija aplicando el cruce de orden.

La solución debe:

- Copiar en el hijo los elementos del padre situados entre los dos puntos de corte.
- Rellenar el resto del hijo con elementos de la madre.
- Comenzar el recorrido de la madre a partir del segundo punto de corte.
- Evitar insertar elementos repetidos.
- Devolver una lista con la misma longitud que las listas originales.

## Formato de entrada

La entrada estándar contiene cuatro líneas:

```
padre
madre
lower_bound
upper_bound
```

donde:

- `padre`: lista de enteros separados por comas.
- `madre`: lista de enteros separados por comas.
- `lower_bound`: índice inferior del segmento que se copia desde el padre.
- `upper_bound`: índice superior del segmento que se copia desde el padre.

El índice `lower_bound` está incluido en el segmento, mientras que `upper_bound` no está incluido, siguiendo la notación habitual de Python:

```
padre[lower_bound:upper_bound]
```

**Ejemplo de entrada:**

```
8,11,3,5,6,4,2,12,1,9,7,10
1,2,3,4,5,6,7,8,9,10,11,12
6
9
```

## Formato de salida

La salida debe ser una única línea con la lista hija resultante, usando el formato estándar de listas de Python.

**Ejemplo:**

```
[4, 5, 6, 7, 8, 9, 2, 12, 1, 10, 11, 3]
```

> La comparación de salida en el VPL es literal, por lo que deben coincidir los corchetes, comas, espacios y saltos de línea.

## Ejemplo de caso de prueba

**Entrada:**

```
8,11,3,5,6,4,2,12,1,9,7,10
1,2,3,4,5,6,7,8,9,10,11,12
6
9
```

**Salida esperada:**

```
[4, 5, 6, 7, 8, 9, 2, 12, 1, 10, 11, 3]
```

**Explicación del ejemplo:**

```
padre = [8, 11, 3, 5, 6, 4, [2, 12, 1], 9, 7, 10]
madre = [1, 2, [3, 4, 5, 6, 7, 8, 9] [10, 11], 12]

lower_bound = 6   # límite inferior
upper_bound = 9   # límite superior
```

Se copia el segmento `[2, 12, 1]` del padre en las posiciones 6-8 del hijo. Luego se rellenan las posiciones libres del hijo recorriendo la madre desde el `upper_bound`, saltando los elementos ya usados, obteniendo:

```
[4, 5, 6, 7, 8, 9, 2, 12, 1, 10, 11, 3]
```

## Tarea del alumno

El alumno debe implementar la lógica del cruce de orden en el archivo `solve.py`.

**Archivos principales:**

- `main.py`: se encarga de leer los datos de entrada, convertirlos a los tipos adecuados, llamar a la función de solución y formatear la salida.
- `solve.py`: contiene la función que debe implementar el alumno.
- `utils.py`: contiene funciones auxiliares para leer la entrada.
- `vpl_evaluate.cases`: contiene los casos de prueba usados por el evaluador.

**Función a implementar:**

```python
def order_crossover(parent1, parent2, lower_bound, upper_bound):
    """Devuelve el hijo generado mediante cruce de orden."""
```

La función debe devolver una lista con el hijo generado.

**Parámetros:**

- `parent1`: lista padre.
- `parent2`: lista madre.
- `lower_bound`: límite inferior del segmento copiado desde `parent1`.
- `upper_bound`: límite superior no incluido del segmento copiado desde `parent1`.

**La función debe:**

- Devolver una lista, no imprimirla directamente.
- No leer datos desde teclado dentro de `solve.py`.
- Mantener la longitud de las listas originales.
- Evitar duplicar elementos.
- Respetar el segmento copiado desde el padre.
- Usar la madre para completar el resto del hijo en orden circular.
