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

    def merge(list, left, mid, right):
        left_copy = list[left:mid +1]
        right_copy = list[mid+1:right +1]

        left_counter = 0
        right_counter = 0
        ordered_counter = left

        while (left_counter < len(left_copy)) and (right_counter < len(right_copy)):
            if left_copy[left_counter][1] < right_copy[right_counter][1]:
                list[ordered_counter] = left_copy[left_counter]
                left_counter += 1
            elif left_copy[left_counter][1] > right_copy[right_counter][1]:
                list[ordered_counter] = right_copy[right_counter]
                right_counter += 1
            else:
                if use_energy:
                    if left_copy[left_counter][2] >= right_copy[right_counter][2]:
                        list[ordered_counter] = left_copy[left_counter]
                        left_counter += 1
                    else:
                        list[ordered_counter] = right_copy[right_counter]
                        right_counter += 1
                else:
                    list[ordered_counter] = left_copy[left_counter]
                    left_counter += 1
            ordered_counter += 1

        while (left_counter < len(left_copy)):
            list[ordered_counter] = left_copy[left_counter]
            left_counter += 1
            ordered_counter += 1

        while (right_counter < len(right_copy)):
            list[ordered_counter] = right_copy[right_counter]
            right_counter += 1
            ordered_counter += 1
        return
        

    def merge_sort(list:list, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(list, left, mid)
            merge_sort(list, mid+1, right)
            merge(list, left, mid, right)
        return


    merge_sort(tracks, 0, len(tracks)-1)
    track_list = []
    for track in tracks:
        track_list.append(track[0])
    return track_list
