from node import *

def solve_branch_and_bound_DFS(capacity, items, record_visiting_order = False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: best_solution.value, best_solution.taken, visiting_order
    """

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.
    alive = []
    
    # Utilizamos la lista Visiting_Order como el registro de nodos visitados
    visiting_order = []

    # Creamos el nodo raiz 
    nodo_raiz = Node(0, [], 0, capacity)

    # Creamos best solution
    best_solution = nodo_raiz

    # Lo añadimos a la lista de nodos vivos (alive)
    alive.append(nodo_raiz)

    # Mientras haya nodos en la lista de nodos vivos
    while alive != []:   
        # Avanzamos al siguiente nodo y lo registramos en nuestro recorrido DFS.
        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)

        if current.value > best_solution.value and current.room >= 0:
            best_solution = current

        # Si no hemos llegado al final del árbol
        if current.index != len(items):
        #    1) Ramificamos (branch) por la derecha (append) si hay room y si el estimate es bueno
            right_node = Node(current.index + 1, current.taken, current.value, current.room)
            if right_node.room >= 0 and Node.estimate(right_node, items) >= best_solution.value:
                alive.append(right_node)
        #    2) Ramificamos (branch) por la izquierda (append) si hay room y si el estimate es bueno
            left_node = Node(current.index + 1, current.taken + [items[current.index].index], current.value + items[current.index].value, current.room-items[current.index].weight)
            if left_node.room >= 0 and Node.estimate(left_node ,items) >= best_solution.value:
                alive.append(left_node)

    


    return best_solution.value, best_solution.taken, visiting_order