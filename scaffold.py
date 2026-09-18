#!/usr/bin/env python3
"""
Automatiza la estructura de carpetas del repo ULPGC_GII_AP
(Algoritmos y Programación).

MODO 1 - Crear carpetas de semanas vacías (al principio de curso,
cuando aún no sabes cuántos ni cuáles ejercicios tocarán):

    python scaffold.py semanas 1 10
    -> crea "Semana 1" ... "Semana 10" vacías

MODO 2 - Crear la estructura completa de un ejercicio a mano, pasando
los .py y el enunciado (.md) uno a uno:

    python scaffold.py ejercicio 1 a "Manejo de arrays" main.py solve.py utils.py --enunciado enunciado.md

MODO 3 - Detección automática: busca en cada carpeta "Semana N" pares
de un .zip y un .md que compartan el mismo prefijo "SxY_" (aunque el
resto del nombre no coincida, p. ej. "S1a_ Manejo de arrays.zip" y
"S1a_Manejo_de_arrays.md"), y para cada par:

    - crea la carpeta del ejercicio con el mismo nombre que el .zip
      (sin la extensión), p. ej. "S1a_ Manejo de arrays"
    - extrae ahí los .py del zip (van sueltos en su raíz)
    - copia esos .py también a las carpetas gabi/ y joseangel/
    - copia el .md dentro, conservando su nombre original
    - borra el .zip y el .md originales

    python scaffold.py auto

Ejecuta el script desde la raíz del repo (donde están las carpetas
"Semana N").
"""

import argparse
import re
import shutil
import zipfile
from pathlib import Path

# Cambia esto si en algún momento cambian las personas del grupo
PERSONAS = ["gabi", "joseangel"]

# Prefijo tipo "S1a_", "S12b_", etc. Es lo único que tiene que coincidir
# entre el zip y el md de un mismo ejercicio.
PREFIJO_RE = re.compile(r"^(S\d+[a-zA-Z]+_)")


def crear_semanas(inicio: int, fin: int, base: Path):
    for n in range(inicio, fin + 1):
        carpeta = base / f"Semana {n}"
        carpeta.mkdir(parents=True, exist_ok=True)
        print(f"✓ {carpeta}")


def _copiar_archivos(archivos, destino: Path):
    for archivo in archivos:
        origen = Path(archivo)
        if not origen.exists():
            print(f"⚠ No encuentro {origen}, lo salto")
            continue
        shutil.copy(origen, destino / origen.name)


def crear_ejercicio(semana: int, letra: str, nombre: str, archivos: list,
                     enunciado, base: Path):
    nombre_carpeta = f"S{semana}{letra} {nombre}"
    carpeta_ejercicio = base / f"Semana {semana}" / nombre_carpeta
    carpeta_ejercicio.mkdir(parents=True, exist_ok=True)

    # Copia base en la raíz del ejercicio
    _copiar_archivos(archivos, carpeta_ejercicio)

    # Copia en cada carpeta de persona
    for persona in PERSONAS:
        carpeta_persona = carpeta_ejercicio / persona
        carpeta_persona.mkdir(exist_ok=True)
        _copiar_archivos(archivos, carpeta_persona)

    # Enunciado, renombrado con el patrón SxY_Nombre_del_ejercicio.md
    if enunciado:
        origen_enun = Path(enunciado)
        if origen_enun.exists():
            nombre_md = f"S{semana}{letra}_{nombre.replace(' ', '_')}.md"
            shutil.copy(origen_enun, carpeta_ejercicio / nombre_md)
        else:
            print(f"⚠ No encuentro el enunciado {origen_enun}")

    print(f"✓ Estructura creada en {carpeta_ejercicio}")


def _prefijo(nombre_archivo: str):
    m = PREFIJO_RE.match(nombre_archivo)
    return m.group(1) if m else None


def _procesar_par(zip_path: Path, md_path: Path, carpeta_semana: Path):
    carpeta_ejercicio = carpeta_semana / zip_path.stem
    carpeta_ejercicio.mkdir(parents=True, exist_ok=True)

    # Extraer los .py del zip (van sueltos en su raíz) a la carpeta del ejercicio
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(carpeta_ejercicio)

    archivos_extraidos = [f for f in carpeta_ejercicio.iterdir() if f.is_file()]

    # Copiar esos archivos a cada carpeta de persona
    for persona in PERSONAS:
        carpeta_persona = carpeta_ejercicio / persona
        carpeta_persona.mkdir(exist_ok=True)
        for f in archivos_extraidos:
            shutil.copy(f, carpeta_persona / f.name)

    # Copiar el enunciado dentro, conservando su nombre original
    shutil.copy(md_path, carpeta_ejercicio / md_path.name)

    # Borrar los originales una vez todo está copiado
    zip_path.unlink()
    md_path.unlink()

    print(f"✓ Procesado automáticamente: {carpeta_ejercicio}")


def procesar_auto(base: Path):
    semanas = sorted(
        p for p in base.iterdir() if p.is_dir() and p.name.startswith("Semana ")
    )
    if not semanas:
        print("No encuentro ninguna carpeta 'Semana N' en el directorio actual.")
        return

    for carpeta_semana in semanas:
        archivos = [f for f in carpeta_semana.iterdir() if f.is_file()]

        grupos = {}
        for f in archivos:
            prefijo = _prefijo(f.name)
            if prefijo:
                grupos.setdefault(prefijo, []).append(f)

        for prefijo, ficheros in grupos.items():
            zips = [f for f in ficheros if f.suffix.lower() == ".zip"]
            mds = [f for f in ficheros if f.suffix.lower() == ".md"]

            if len(zips) == 1 and len(mds) == 1:
                _procesar_par(zips[0], mds[0], carpeta_semana)
            elif zips or mds:
                print(
                    f"⚠ {carpeta_semana.name}: prefijo '{prefijo}' incompleto "
                    f"({len(zips)} zip, {len(mds)} md), lo salto"
                )


def main():
    parser = argparse.ArgumentParser(description="Automatiza el repo de AP")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_semanas = sub.add_parser("semanas", help="Crear carpetas de semanas vacías")
    p_semanas.add_argument("inicio", type=int)
    p_semanas.add_argument("fin", type=int)

    p_ej = sub.add_parser("ejercicio", help="Crear la estructura completa de un ejercicio a mano")
    p_ej.add_argument("semana", type=int)
    p_ej.add_argument("letra", help='p. ej. "a", "b"')
    p_ej.add_argument("nombre", help='p. ej. "Manejo de arrays"')
    p_ej.add_argument("archivos", nargs="+", help="Rutas a los .py base descargados de Moodle")
    p_ej.add_argument("--enunciado", default=None, help="Ruta al enunciado ya convertido a .md")

    sub.add_parser("auto", help="Detectar pares zip+md por prefijo y montar la estructura")

    args = parser.parse_args()
    base = Path(".")

    if args.comando == "semanas":
        crear_semanas(args.inicio, args.fin, base)
    elif args.comando == "ejercicio":
        crear_ejercicio(args.semana, args.letra, args.nombre, args.archivos, args.enunciado, base)
    elif args.comando == "auto":
        procesar_auto(base)


if __name__ == "__main__":
    main()
