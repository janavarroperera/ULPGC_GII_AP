# S8.3 MergeSort DJ Playlist (BPM + Flow)

- **Límite de entrega:** domingo, 15 de noviembre de 2026, 23:59
- **Ficheros requeridos:** `main.py`, `solve.py`, `utils.py`
- **Número máximo de ficheros:** 4
- **Tipo de trabajo:** Individual

## Contexto

Un DJ quiere ordenar canciones por **BPM** (*beats per minute*), pero desea preservar el **orden de entrada** en las canciones que empatan en BPM (para mantener el *flow* de la sesión).

## Objetivo

**Comparador compuesto:** Si además se proporciona un campo **energía** (entero), en caso de empate de BPM se ordena por **energía descendente**; si aún empatan, entonces se preserva el **orden de llegada (estabilidad)**:

- Si se incluye `energy` (en todas las líneas o en ninguna), el comparador será **BPM ascendente, energy descendente y estable**.
- Si **NO** hay `energy`, el comparador es solo **BPM ascendente y estable**.

## Formato de entrada

```
N
title_1 bpm_1 [energy_1]
...
title_N bpm_N [energy_N]
```

donde:

- `N` entero > 0.
- Cada línea tiene **2** o **3** tokens:
  - `title`: texto **sin espacios** con el título de la pista.
  - `bpm`: entero (>= 0).
  - `[energy]` (opcional): entero (mayor suele implicar pista "más enérgica").

## Formato de salida

Una sola línea que contiene la **lista de títulos ordenados**:

```
[title_ordenado_1, title_ordenado_2, ..., title_ordenado_N]
```

## Ejemplo de caso de prueba

### Ejemplo (sin energy)

**Entrada**

```
5
Track9 128
Track3 124
Track7 128
Track1 120
Track8 130
```

**Salida esperada** (estabilidad: `Track9` antes que `Track7`)

```
[Track1, Track3, Track9, Track7, Track8]
```

### Ejemplo (con energy)

**Entrada**

```
5
Track1 128 50
Track2 128 70
Track3 125 90
Track4 128 70
Track5 130 40
```

**Salida esperada** (BPM asc; empates por energía desc; empate perfecto conserva orden de entrada: `Track2` antes que `Track4`)

```
[Track3, Track2, Track4, Track1, Track5]
```

### Diagrama del caso `c02` — MergeSort (BPM asc, estable)

El diagrama se sigue de arriba hacia abajo; en empate de la clave completa, se mantiene el orden de entrada. Leyenda: azul = Entrada; gris = Hoja (1 elemento); amarillo = Merge intermedio; verde = Solución ordenada.

| Nivel | Contenido |
|---|---|
| **ENTRADA** | `[Track9 (128), Track3 (124), Track7 (128), Track1 (120), Track8 (130)]` |
| **DIVISIÓN 1** | `[Track9 (128), Track3 (124)]` y `[Track7 (128), Track1 (120), Track8 (130)]` |
| **DIVISIÓN 2** | `[Track9]`, `[Track3]`, `[Track7]` y `[Track1 (120), Track8 (130)]` |
| **CASOS BASE** | `[Track9]`, `[Track3]`, `[Track7]`, `[Track1]`, `[Track8]` (hojas de 1 elemento) |
| **FUSIÓN 1** | `[Track9]`, `[Track3]`, `[Track7]` (sin cambios) y `[Track1 (120), Track8 (130)]` (resultado de fusionar `[Track1]` y `[Track8]`) |
| **FUSIÓN 2** | `[Track3 (124), Track9 (128)]` (de fusionar `[Track9]` y `[Track3]`) y `[Track1 (120), Track7 (128), Track8 (130)]` (de fusionar `[Track7]` y `[Track1, Track8]`) |
| **SOLUCIÓN** | `[Track1 (120), Track3 (124), Track9 (128), Track7 (128), Track8 (130)]` |

Nota del diagrama: los nodos grises repetidos solo conservan la canción; no representan nuevas divisiones.

Solución mostrada: `[Track1, Track3, Track9, Track7, Track8]`

## Tarea del alumno

Implementar la siguiente función en el fichero `solve.py` para ordenar las canciones usando **MergeSort estable**:

```python
def sort_playlist_by_flow(tracks, use_energy):
    """
    Parámetros:
      - tracks: lista de tuplas (title:str, bpm:int [, energy:int])
      - use_energy: bool (True si todas las líneas incluyen energy)
    Devuelve:
      - list[str]: títulos en el orden final
    Reglas del comparador:
      - Siempre BPM **ascendente**.
      - Si use_energy: en empate de BPM, **energy descendente**.
      - Si vuelve a haber empate, mantener **orden de llegada** (estabilidad).
    """
```

El fichero `main.py` (proporcionado):

- Lee `N` y, a continuación, las `N` canciones, una por línea, con su **título**, su **BPM** y, opcionalmente, su **energy** (detecta automáticamente si se ha proporcionado según el número de tokens de cada línea que será el mismo en todas ellas).
- Llama a `sort_playlist_by_flow()` en `solve.py` y **formatea** la salida como `[Track1, Track2, ...]` (solo títulos) para verficar que cumple con lo esperado en los casos de prueba (con y sin energy).

### Estrategía requerida: MergeSort estable

- Un algoritmo de ordenación es **estable** si, cuando dos elementos tienen la **misma clave de ordenación** (aquí, mismo `bpm` y, si procede, misma `energy`), se **mantiene su orden relativo de entrada** en la salida.
- En **MergeSort**, la estabilidad se garantiza en la fase de `merge(left, right)` eligiendo en caso de empate el **elemento del subarray izquierdo** primero.
- **Consideraciones**:
  - Si solo se ordena por `bpm`, dos pistas con el mismo `bpm` conservarán el orden en que aparecieron en la entrada.
  - Si además se usa `energy` como desempate (descendente), solo cuando `bpm` y `energy` empatan se preserva el orden de llegada.
