# Algoritmos y Programación — S2a: Manejo de strings

**Límite de entrega:** domingo, 27 de septiembre de 2026, 23:59
**Ficheros requeridos:** `main.py`, `solve.py`, `utils.py`
**Tipo de trabajo:** Individual

## Contexto

En este ejercicio, la entrada del programa está formada por varias líneas de texto con letras y números. Los números pueden aparecer de dos formas:

- como dígitos: 1, 2, 3, 4, 5, 6, 7, 8, 9;
- como texto en inglés: one, two, three, four, five, six, seven, eight, nine.

En cada línea hay que combinar el primer y el último dígito encontrados, en ese orden, para formar un número de dos dígitos.

## Objetivo

Escribir el código en Python que calcule la suma de todos los números de dos dígitos asociados a todas las líneas de texto de la entrada.

Por ejemplo, para estas líneas:

```
two1nine
abcone2cdthreexyz
xtwone3fo
treb7uchzoneet
```

los números de dos dígitos son:

```
29, 13, 23, 71
```

y el resultado final es:

```
29 + 13 + 23 + 71 = 136
```

## Formato de entrada

La entrada estándar tiene el siguiente formato:

```
N
linea1
linea2
...
lineaN
```

donde:

- `N` es el número de líneas de texto que se deben procesar.
- Las siguientes `N` líneas son las strings que contienen letras y números.

Ejemplo de entrada:

```
4
two1nine
abcone2cdthreexyz
xtwone3fo
treb7uchzoneet
```

## Formato de salida

Se debe imprimir un único entero: la suma de todos los números de dos dígitos obtenidos a partir de las líneas de entrada.

## Ejemplo de caso de prueba

**Entrada:**

```
4
two1nine
abcone2cdthreexyz
xtwone3fo
treb7uchzoneet
```

**Salida esperada:**

```
136
```

**Explicación:**

- `two1nine` produce 29.
- `abcone2cdthreexyz` produce 13.
- `xtwone3fo` produce 23.
- `treb7uchzoneet` produce 71.
- La suma es 29 + 13 + 23 + 71 = 136.

## Tarea del alumno

El alumno debe implementar la función `solve(input_list)` en `solve.py`.

**Archivos principales:**

- `main.py`: lee la entrada, prepara la lista de strings, llama a `solve(input_list)` e imprime el resultado.
- `solve.py`: contiene la función que debe completar el alumno.
- `vpl_evaluate.cases`: contiene los casos de prueba usados por el evaluador automático.

La función esperada es:

```python
def solve(input_list):
    """Devuelve la suma total de los valores de calibración."""
```

La función recibe como parámetro una lista de strings y debe devolver un entero con la suma total.

### Estrategia requerida

Para cada línea, se debe localizar:

1. el primer número que aparece en la string;
2. el último número que aparece en la string.

Cada número puede estar escrito como dígito o como palabra en inglés. Después se forma un número de dos cifras y se acumula en la suma total.

Las palabras pueden solaparse. Por ejemplo:

- `"twone"` contiene "two" y "one", por tanto produce 21.
- `"oneight"` contiene "one" y "eight", por tanto produce 18.

### Pistas y consideraciones

- No se debe usar `input()` dentro de `solve`.
- No se debe usar `print()` dentro de `solve`.
- `solve` debe devolver un entero.
- `main.py` ya se encarga de leer la entrada y mostrar la salida.
- Hay que tener cuidado con casos en los que aparecen varios números dentro de la misma línea.
