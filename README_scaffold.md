# scaffold.py

Script para automatizar la estructura de carpetas del repo de ejercicios de
Algoritmos y Programación (ULPGC_GII_AP).

## Estructura del repo

```
Semana 1/
  S1a_ Manejo de arrays/
    main.py
    solve.py
    utils.py
    S1a_Manejo_de_arrays.md
    gabi/
      main.py
      solve.py
      utils.py
    joseangel/
      main.py
      solve.py
      utils.py
Semana 2/
  ...
```

Cada ejercicio tiene los `.py` base sueltos en la raíz de su carpeta, el
enunciado en `.md`, y una copia de los `.py` por cada persona (`gabi` y
`joseangel`, definidas en la constante `PERSONAS` al principio del script —
edítala ahí si cambia el equipo).

Ejecuta siempre el script desde la raíz del repo, donde están las carpetas
`Semana N`:

```
python scaffold.py <comando> ...
```

## Modo `semanas` — crear semanas vacías

Al empezar el curso, cuando aún no sabes cuántos ni cuáles ejercicios van a
caer:

```
python scaffold.py semanas 1 10
```

Crea `Semana 1` a `Semana 10` vacías.

## Modo `ejercicio` — crear un ejercicio a mano

Cuando ya tienes el enunciado en `.md` y los `.py` base descargados de
Moodle, y quieres montar la estructura pasando cada archivo por su ruta:

```
python scaffold.py ejercicio 1 a "Manejo de arrays" main.py solve.py utils.py --enunciado enunciado.md
```

| Parte | Significado |
|---|---|
| `1` | Número de semana → `Semana 1` |
| `a` | Letra del ejercicio → junto con la semana forma `S1a` |
| `"Manejo de arrays"` | Nombre del ejercicio (entre comillas si tiene espacios) |
| `main.py solve.py utils.py` | Rutas a los `.py` base, tantos como necesites |
| `--enunciado enunciado.md` | Ruta al enunciado ya convertido a `.md` |

Crea `Semana 1/S1a Manejo de arrays/` con los `.py` en la raíz, el enunciado
renombrado a `S1a_Manejo_de_arrays.md`, y copias en `gabi/` y `joseangel/`.

## Modo `auto` — detección automática (el habitual)

El modo pensado para el uso normal: descargas de Moodle el `.zip` con los
`.py` del ejercicio y el enunciado en `.md`, los dejas sueltos dentro de la
carpeta `Semana N` correspondiente, y ejecutas:

```
python scaffold.py auto
```

El script recorre todas las carpetas `Semana N` del repo. En cada una:

1. Agrupa los archivos por su **prefijo** `SxY_` (ej. `S1a_`, `S12b_`).
   El zip y el md de un mismo ejercicio no tienen por qué compartir nombre
   completo — basta con que compartan ese prefijo. Por ejemplo:
   - `S1a_ Manejo de arrays.zip`
   - `S1a_Manejo_de_arrays.md`
2. Si para un prefijo encuentra exactamente un `.zip` y un `.md`:
   - Crea la carpeta del ejercicio con el **nombre del zip** (sin la
     extensión) → `Semana 1/S1a_ Manejo de arrays/`
   - Extrae ahí los `.py` del zip (deben ir sueltos en su raíz, sin
     subcarpetas dentro del zip)
   - Copia esos `.py` también a `gabi/` y `joseangel/`
   - Copia el `.md` dentro de la carpeta, **conservando su nombre original**
     (no se renombra)
   - **Borra el `.zip` y el `.md` originales**
3. Si un prefijo tiene zip sin md (o al revés), avisa por consola y lo salta
   sin tocar nada.
4. Carpetas de ejercicios que ya estén montadas (sin zip/md sueltos) se
   ignoran.

Puede haber varios pares zip+md a la vez en la misma semana; cada uno se
procesa de forma independiente.

⚠️ **El borrado del zip y el md es irreversible.** Si quieres probarlo antes
de correrlo sobre el repo real, hazlo primero sobre una copia de una semana.

## Requisitos

Solo librería estándar de Python 3 (`argparse`, `pathlib`, `shutil`,
`zipfile`, `re`). No hace falta instalar nada.
