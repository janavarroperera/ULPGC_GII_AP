# Esqueleto para ejercicio del VPL
from typing import List

def solve_mfd_feasible(exams: List[int], rooms: List[int]):
  """

  Objetivo propuesto:
  Implementar la estrategia MFD (Max-Fit Decreasing)
  para asignar exámenes a aulas con formato de salida esperado:

  "rooms_used=<k> waste=<w>\nassign=[cap1, cap2, ...]"

  donde 'assign[i]' -> capacidad del aula asignada al examen 'exams[i]'.

  Parámetros:
    - exams: lista de enteros con los tamaños/necesidades de cada examen.
    - rooms: lista de enteros con las capacidades de las aulas disponibles.

  Devuelve:
    - (rooms_used, waste, assign_cap) si es factible
    - None si no hay asignación posible

  Implementación de estrategia MFD:
    - Ordenar exámenes de mayor a menor.
    - Ordenar aulas de mayor a menor.
    - Asignar secuencialmente la primera aula suficientemente grande a cada examen.
    - Calcular rooms_used, waste y la lista assign en el orden original de exams.
  """

  exams.sort(reverse=True)
  rooms.sort(reverse=True)

  # print(exams)
  # print(rooms)

  results= []
  

  for exam in exams:
    for room in rooms:
      if exam <= room:
        results.append([exam, room])
        rooms.remove(room)
        break

  if len(results) < len(exams): return None

  # print(results)

  rooms_used = len(results)

  
  waste = 0
  for result in results:
    temp_waste = result[1] - result[0]
    waste += temp_waste

  assign_cap = []
  for result in results:
    assign_cap.append(result[1])

  return(rooms_used, waste, assign_cap)


  # Valor por defecto: indicar que no hay solución.
  return None

