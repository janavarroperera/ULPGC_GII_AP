# S9.2b: MiniZinc: xoptima.mzn

- **Límite de entrega:** domingo, 15 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `xoptima.mzn`
- **Tipo de trabajo:** Individual

## Contexto

MiniZinc permite definir variables de decisión, establecer restricciones y optimizar una función objetivo.

## Objetivo

Desarrollar un modelo de optimización en MiniZinc que determine el valor de una variable que cumpla unas condiciones dadas.

## Formato de entrada

El enunciado no especifica entrada (el modelo no recibe datos).

## Formato de salida

El programa deberá mostrar:

```
x=valor de x obj=valor de obj
```

> Nota: en el PDF el formato aparece en una sola línea; podría corresponder a dos líneas en el original.

## Ejemplo de caso de prueba

El enunciado no incluye ejemplos.

## Tarea del alumno

Construir un modelo `xoptima.mzn` que:

- Defina una variable de decisión `x` en el rango de 0 a 10.
- Imponga la restricción de que `x` sea divisible por 4.
- Minimice la función objetivo `(x-7)^2`. Usar `pow(_,_)`.
- Muestre el valor de `x` y el valor de la función objetivo `obj`.
