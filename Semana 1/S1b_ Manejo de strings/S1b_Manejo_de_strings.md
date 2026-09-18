# Algoritmos y Programación — S1b: Manejo de strings

**Límite de entrega:** domingo, 20 de septiembre de 2026, 23:59
**Ficheros requeridos:** `main.py`, `solve.py`, `utils.py` (se descargan aparte)
**Tipo de trabajo:** Individual

## Contexto

En este ejercicio, la entrada del programa son varias líneas de texto con letras y números. En cada línea debemos combinar el primer y el último dígito (en este orden) para formar un número de dos dígitos.

Para cada cadena:

- se localiza el primer dígito que aparece en la cadena,
- se localiza el último dígito que aparece en la cadena,
- se forma un número de dos cifras con ambos dígitos,
- se suma ese número al total.

Si una cadena solo contiene un dígito, ese dígito se usa como primera y como última cifra. Si una cadena no contiene ningún dígito, no aporta nada a la suma.

Por ejemplo, suponiendo estas líneas:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

Los números de dos dígitos de estas cuatro líneas son 12, 38, 15 y 77. El resultado que debe generar el programa es su suma:

```
12 + 38 + 15 + 77 = 142
```

Como muestra `treb7uchet`, si una línea contiene un único dígito, ese mismo dígito se utiliza como primero y como último.

## Objetivo

Escribir el código en Python que calcule la suma de todos los números de dos dígitos asociados a todas las líneas de texto de la entrada.

## Formato de entrada

- La primera línea es un descriptor: el número de líneas de texto que se van a procesar (`N`).
- El resto de las líneas son las cadenas de texto.

```
N
linea_1
linea_2
...
linea_N
```

## Formato de salida

El programa debe imprimir un único número entero: la suma de los números obtenidos al combinar el primer y el último dígito de cada línea.

## Ejemplo de caso de prueba

**Entrada:**

```
4
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

**Salida esperada:**

```
142
```

## Tarea del alumno

El alumno debe completar la función `solve` en `solve.py`:

```python
def solve(input_list):
    pass
```

La función recibe una lista de cadenas y debe devolver un entero con la suma solicitada. No debe leer por teclado ni imprimir resultados, porque `main.py` se encarga de la entrada y la salida.

**Archivos principales:**

- `main.py`: lee el número de líneas, prepara la lista de cadenas y muestra el resultado.
- `solve.py`: contiene la función `solve(input_list)` que debe completar el alumno.
- `vpl_evaluate.cases`: contiene los casos usados por la evaluación automática.

### Estrategia requerida

Recorrer cada cadena carácter a carácter para identificar sus dígitos. Después, combinar el primer y el último dígito encontrados y acumular el número resultante.

### Pistas y consideraciones

- El método `str.isdigit()` permite comprobar si un carácter es un dígito.
- Convertir dos caracteres numéricos concatenados con `int(...)` produce el número de dos cifras correspondiente.
- No es necesario modificar `main.py` para resolver el ejercicio.
