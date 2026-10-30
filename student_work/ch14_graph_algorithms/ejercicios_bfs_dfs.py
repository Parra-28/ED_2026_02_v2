from goodrich.ch14.graph import Graph

def vecinos(g, v):
    resultado = []
    for e in g.incident_edges(v):
        w = e.opposite(v)
        resultado.append(w.element())
    return resultado


def dfs(g, v, d):
    for e in g.incident_edges(v):
        w = e.opposite(v)
        if w not in d:
            d[w] = e
            dfs(g, w, d)


def bfs(g, v):
    d = {v: None}
    nivel = [v]
    while len(nivel) > 0:
        siguiente_nivel = []
        for u in nivel:
            for e in g.incident_edges(u):
                w = e.opposite(u)
                if w not in d:
                    d[w] = e
                    siguiente_nivel.append(w)
        nivel = siguiente_nivel
    return d


def alcanzables(g, v):
    descubiertos = bfs(g, v)
    return [w.element() for w in descubiertos.keys()]


if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
