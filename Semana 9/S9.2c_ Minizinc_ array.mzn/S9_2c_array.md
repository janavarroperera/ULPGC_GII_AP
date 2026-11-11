# S9.2c: MiniZinc: array.mzn

- **Límite de entrega:** domingo, 15 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `array.mzn`
- **Tipo de trabajo:** Individual

## Contexto

En este ejercicio se trabajará con arrays en MiniZinc, definiendo arrays de variables de decisión y estableciendo restricciones sobre sus elementos para obtener una solución óptima.

## Objetivo

- Declarar un array de longitud 5 con variables de decisión cuyos valores estén entre 1 y 9.
- Establecer que la suma de los elementos sea igual a su producto.
- Añadir una restricción para que los valores estén ordenados de forma creciente.
- Maximizar el producto de los elementos del array.

## Formato de entrada

El enunciado no especifica entrada (el parámetro `n = 5` se define en el propio modelo).

## Formato de salida

El programa debe mostrar el array resultante con el siguiente formato:

```
x = array1d(1..5, [valores de x]);
```

## Ejemplo de caso de prueba

El enunciado no incluye ejemplos.

## Tarea del alumno

Crear un modelo `array.mzn` que cumpla las siguientes condiciones:

- Definir el parámetro `n = 5`, que establece la longitud del array.
- Declarar un array `x` de variables de decisión con valores entre 1 y 9.
- Imponer la restricción de que la suma de los elementos sea igual al producto de los mismos.
- Imponer que los elementos estén ordenados de forma creciente: `x[1] <= x[2] <= ... <= x[n]`
- Utilizar una función objetivo que maximice el producto de los elementos de `x`.
