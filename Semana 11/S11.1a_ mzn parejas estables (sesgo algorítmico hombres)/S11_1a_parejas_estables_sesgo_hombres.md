# S11.1a: mzn parejas estables (sesgo algorítmico, hombres)

> **Límite de entrega:** domingo, 29 de noviembre de 2026, 23:59
> **Ficheros requeridos:** `stable_matching.mzn`
> **Tipo de trabajo:** Individual

## Contexto

Problema de **parejas estables** (stable matching) visto en clase, resuelto con MiniZinc. Se dispone de un conjunto de mujeres (`Women`) y otro de hombres (`Men`), cada uno con sus preferencias sobre el otro grupo.

## Objetivo

Resolver el problema de parejas estables **maximizando el número de hombres que obtienen como esposa su primera opción**.

## Formato de entrada

Datos en formato MiniZinc:

- `Women`: enumerado con los nombres de las mujeres.
- `Men`: enumerado con los nombres de los hombres.
- `wrank`: matriz `[Women, Men]` de enteros. Preferencia de cada mujer sobre cada hombre (1 = primera opción).
- `mrank`: matriz `[Men, Women]` de enteros. Preferencia de cada hombre sobre cada mujer (1 = primera opción).

## Formato de salida

Se imprimen, por este orden:

- `wife`: lista con la esposa asignada a cada hombre (en el orden de `Men`).
- `husband`: lista con el marido asignado a cada mujer (en el orden de `Women`).
- `obj_men`: valor del objetivo para los hombres.
- `obj_women`: valor del objetivo para las mujeres.
- Separadores de solución de MiniZinc: `----------` y, al final, `==========`.

## Ejemplo de caso de prueba

**Input:**

```
Women = {Ana, Marta, Patricia};
Men = {Carlos, Marco, Juan};
wrank= [|1, 2, 3,
|3, 2, 1,
|3, 1, 2
|];
mrank= [|2, 1, 3,
 |1, 2, 3,
 |1, 3, 2
 |];
```

**Output:**

```
wife : [Marta, Ana, Patricia]
husband: [Marco, Carlos, Juan]
obj_men:2
obj_women:0
----------
==========
```

que se interpreta como:

```
mrank[Marco, Ana]==1:true
mrank[Carlos, Marta]==1:true
mrank[Juan, Patricia]==1:false
wife[Marco]:Ana
wife[Carlos]:Marta
wife[Juan]:Patricia
husband[Ana]:Marco
husband[Marta]:Carlos
husband[Patricia]:Juan
```

## Tarea del alumno

Completar el fichero `stable_matching.mzn`, que se descarga con el botón "Descargar" y ya declara `Women`, `Men`, `wrank` y `mrank`. El código propio se escribe a partir del comentario `%Escribir el código a partir de aquí`.
