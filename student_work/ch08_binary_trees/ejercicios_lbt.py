from goodrich.ch08.linked_binary_tree import LinkedBinaryTree

def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if T.is_empty():
        return True

    cola = [T.root()]
    encontro_hueco = False

    while cola:
        nodo = cola.pop(0)

        if nodo is None:
            encontro_hueco = True
        else:

            if encontro_hueco:
                return False

            cola.append(T.left(nodo))
            cola.append(T.right(nodo))

    return True


def camino(T, p, q):
    #saca todos los ancestros de un nodo hasta la raíz
    def ancestros(nodo):
        ruta = []
        actual = nodo
        while actual is not None:
            ruta.append(actual)
            actual = T.parent(actual)
        return ruta

    ruta_p = ancestros(p)
    ruta_q = ancestros(q)

    # Encontrar elLCA
    lca = None
    for nodo in ruta_p:
        if nodo in ruta_q:
            lca = nodo
            break

    # Construir el camino final
    camino_final = []

    # desde p hasta el LCA 
    for nodo in ruta_p:
        camino_final.append(str(nodo.element()))
        if nodo == lca:
            break
   #BAJAR
    idx_lca_q = ruta_q.index(lca)
    for i in range(idx_lca_q - 1, -1, -1):
        camino_final.append(str(ruta_q[i].element()))

    return " -> ".join(camino_final)

if __name__ == "__main__":
    pass
