from node import *

def solve_branch_and_bound_DFS(capacity, items, record_visiting_order = False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """

    # Completa este código para realizar el recorrido DFS; tienes
    # indicados los sitios que debes completar con tres puntos
    # suspensivos ("...")

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.

    alive = []
    
    # Utilizamos la lista Visiting_Order como el registro de nodos
    # visitados (el contenido final de esta lista lo utiliza el VPL
    # para comprobar que nuestro recorrido DFS es correcto).

    visiting_order = []

    # 1) Creamos el nodo raiz (en este VPL todavía no utilizamos los
    #    parámetros taken, value, room, con lo que se inicializan con
    #    lista vacía y 0). El único valor necesario en el nodo es el
    #    indice al primer elemento de la lista (index = 0).
    # ...
    root = Node(0, [], 0, capacity)

    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(root)

    best_node:Node = root

    # Mientras haya nodos en la lista de nodos vivos
    # ...
    while len(alive) > 0:  #sustituir el True por la condición que considere más adecuada
        
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current:Node = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)

        if current.value > best_node.value and current.room >= 0:
            best_node = current

        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append)
        #    2) Ramificamos (branch) por la izquierda (append)
        # ...
        if current.index < len(items):
            node_right = Node(current.index +1, current.taken, current.value, current.room)
            node_left = Node(current.index +1, current.taken + [items[current.index].index], current.value + items[current.index].value, current.room - items[current.index].weight)

            if node_right.room >= 0 and node_right.estimate(items):
                alive.append(node_right) # derecha
            if node_left.room >= 0 and node_left.estimate(items):
                alive.append(node_left) # izquierda

    return best_node.value, best_node.taken, visiting_order