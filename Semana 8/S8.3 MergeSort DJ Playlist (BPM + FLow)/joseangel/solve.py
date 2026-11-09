# MergeSort estable para ordenar canciones por BPM (asc), y opcionalmente por energy (desc).
# Devuelve únicamente la lista de títulos ordenados (list[str]).

def sort_playlist_by_flow(tracks, use_energy):
    """
    Ordena una playlist aplicando MergeSort estable por BPM ascendente y, si
    `use_energy` es True, desempatando por energía descendente. Devuelve
    exclusivamente los títulos en el orden final.

    Parámetros:
      - tracks: lista de tuplas (title:str, bpm:int [, energy:int])
      - use_energy: bool → si True, en empates de BPM se usa energy descendente

    Devuelve:
      - list[str]: títulos en el orden final

    Detalles del comparador y estabilidad:
      - Siempre prioriza menor BPM (ascendente).
      - Si `use_energy` es True y el BPM empata, mayor energía primero
        (descendente).
      - Si vuelve a haber empate, se preserva orden de llegada (estabilidad),
        seleccionando el elemento del subarray izquierdo.
    """

    return
