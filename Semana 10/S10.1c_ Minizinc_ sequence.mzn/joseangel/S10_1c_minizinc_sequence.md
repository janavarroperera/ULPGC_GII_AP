# S10.1c: MiniZinc: sequence.mzn

- **Límite de entrega:** domingo, 22 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `sequence.mzn`
- **Tipo de trabajo:** Individual

## Contexto

MiniZinc permite representar secuencias mediante arrays de variables de decisión y establecer restricciones sobre sus elementos y sus relaciones.

## Objetivo

Familiarizarse con la definición y manipulación de arrays de variables de decisión, así como con la formulación de restricciones sobre posiciones concretas y elementos adyacentes.

## Formato de entrada

No aplica (la longitud se fija mediante el parámetro `n = 5` dentro del modelo).

## Formato de salida

El programa deberá mostrar la secuencia obtenida con el siguiente formato:

```
x = [valores de x];
----------
==========
```

## Tarea del alumno

Construir un modelo llamado `sequence.mzn` que genere una secuencia de longitud 5, definida mediante el parámetro `n = 5`.

La secuencia deberá cumplir las siguientes condiciones:

- Cada elemento del array debe ser una variable de decisión con un valor comprendido entre 0 y 3.
- El primer elemento de la secuencia debe ser 0.
- El último elemento de la secuencia debe ser 3.
- La suma de cada pareja de elementos adyacentes no puede superar 3.
- Los elementos situados en posiciones divisibles por 3 deben tener un valor mayor o igual que 2.
- Se deberá maximizar la suma de todos los elementos de la secuencia.

**Ficheros requeridos:** `sequence.mzn`
