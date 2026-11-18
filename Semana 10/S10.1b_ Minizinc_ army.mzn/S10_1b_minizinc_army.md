# S10.1b: MiniZinc: army.mzn

- **Límite de entrega:** domingo, 22 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `army.mzn`
- **Tipo de trabajo:** Individual

## Contexto

MiniZinc permite modelar problemas de optimización mediante variables de decisión, restricciones y funciones objetivo.

## Objetivo

Familiarizarse con la formulación de problemas de optimización, utilizando restricciones presupuestarias y límites en la disponibilidad de recursos.

## Formato de entrada

No aplica (los datos del problema forman parte del enunciado).

## Formato de salida

El programa deberá mostrar el número de soldados reclutados de cada pueblo con el siguiente formato:

```
F = valor;
L = valor;
Z = valor;
J = valor;
----------
==========
```

## Tarea del alumno

Construir un modelo llamado `army.mzn` que permita determinar cómo reclutar soldados de cuatro pueblos distintos (F, L, Z y J) para **maximizar la fuerza total del ejército** sin exceder el presupuesto disponible.

Se dispone de la siguiente información:

| Pueblo | Fuerza por soldado | Coste por soldado | Máximo de soldados |
|:------:|:------------------:|:-----------------:|:------------------:|
| F      | 6                  | 13 $              | 1000               |
| L      | 10                 | 21 $              | 400                |
| Z      | 8                  | 17 $              | 500                |
| J      | 40                 | 100 $             | 150                |

El presupuesto máximo disponible es de **10 000 $**.

**Ficheros requeridos:** `army.mzn`
