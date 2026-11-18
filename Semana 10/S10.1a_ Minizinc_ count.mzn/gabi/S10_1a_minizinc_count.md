# S10.1a: MiniZinc: count.mzn

- **Límite de entrega:** domingo, 22 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `count.mzn`
- **Tipo de trabajo:** Individual

## Contexto

MiniZinc permite modelar problemas de razonamiento aritmético mediante variables de decisión y restricciones.

## Objetivo

Familiarizarse con la definición de variables, la formulación de restricciones y la resolución de problemas de divisibilidad en MiniZinc.

## Formato de entrada

No aplica (el modelo no recibe datos de entrada).

## Formato de salida

El programa deberá mostrar el número de soldados con el siguiente formato:

```
army = valor;
----------
==========
```

## Tarea del alumno

Construir un modelo llamado `count.mzn` que permita determinar cuántos soldados hay en un ejército, sabiendo que:

- El número de soldados está comprendido entre 100 y 500.
- Al formar columnas de 5 soldados, sobran 2.
- Al formar columnas de 7 soldados, sobran 2.
- Al formar columnas de 12 soldados, sobra 1.

La variable de decisión deberá llamarse `army`. **¿Cuántos soldados hay?**

**Ficheros requeridos:** `count.mzn`
