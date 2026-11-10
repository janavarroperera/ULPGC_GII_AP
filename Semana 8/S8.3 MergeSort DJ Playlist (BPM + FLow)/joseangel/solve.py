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

  def merge_sort(lista, left, right):
    if left < right:
      mid = (left + right) // 2

      merge_sort(lista, left, mid)
      merge_sort(lista, mid + 1, right)

      merge(lista, left, right, mid)
    
    return


  def merge(lista, left, right, mid):
    left_cpy = lista[left:mid + 1]
    right_cpy = lista[mid + 1:right + 1]

    l_counter, r_counter = 0,0
    sorted_counter = left


    while l_counter < len(left_cpy) and r_counter < len(right_cpy):
      if left_cpy[l_counter][1] < right_cpy[r_counter][1]:
        lista[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
      elif left_cpy[l_counter][1] > right_cpy[r_counter][1]:
        lista[sorted_counter] = right_cpy[r_counter]
        r_counter += 1
      elif (left_cpy[l_counter][1] == right_cpy[r_counter][1]) and (use_energy == True):
        if left_cpy[l_counter][2] >= right_cpy[r_counter][2]:
          lista[sorted_counter] = left_cpy[l_counter]
          l_counter += 1
        else:
          lista[sorted_counter] = right_cpy[r_counter]
          r_counter += 1
      else:
        lista[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
      sorted_counter += 1

    while l_counter < len(left_cpy):
      lista[sorted_counter] = left_cpy[l_counter]
      l_counter += 1
      sorted_counter += 1

    while r_counter < len(right_cpy):
      lista[sorted_counter] = right_cpy[r_counter]
      r_counter += 1
      sorted_counter += 1

    return


  merge_sort(tracks, 0, len(tracks)-1)


  track_names = []
  for track in tracks:
    track_names.append(track[0])

  return track_names
