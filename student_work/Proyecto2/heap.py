import matplotlib.pyplot as plt
import networkx as nx

class Heap:
    def __init__(self):
        self.arreglo = [float('-inf')]

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.arreglo[i] < self.arreglo[i // 2]:
                self.arreglo[i], self.arreglo[i // 2] = self.arreglo[i // 2], self.arreglo[i]
            i = i // 2

    def _percolate_down(self, i):
        while (i * 2) <= len(self.arreglo) - 1:
            mc = self._min_child(i)
            if self.arreglo[i] > self.arreglo[mc]:
                self.arreglo[i], self.arreglo[mc] = self.arreglo[mc], self.arreglo[i]
            i = mc

    def _min_child(self, i):
        if i * 2 + 1 > len(self.arreglo) - 1:
            return i * 2
        else:
            if self.arreglo[i * 2] < self.arreglo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        self._percolate_up(len(self.arreglo) - 1)
        if imagen:
            self._dibujar()

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) == 1:
            return None
        retval = self.arreglo[1]
        self.arreglo[1] = self.arreglo[len(self.arreglo) - 1]
        self.arreglo.pop()
        self._percolate_down(1)
        if imagen:
            self._dibujar()
        return retval

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + lista[:]
        i = len(lista) // 2
        while i > 0:
            self._percolate_down(i)
            i = i - 1
        if imagen:
            self._dibujar()

    def _dibujar(self):
        if len(self.arreglo) <= 1:
            return

        G = nx.Graph()

        for i in range(1, len(self.arreglo)):
            G.add_node(i, label=str(self.arreglo[i]))
            if i // 2 > 0:
                G.add_edge(i // 2, i)

        def calcular_posiciones(indice, x, y, x_offset):
            pos = {}
            if indice < len(self.arreglo):
                pos[indice] = (x, y)
                pos.update(calcular_posiciones(indice * 2, x - x_offset, y - 1, x_offset / 2))
                pos.update(calcular_posiciones(indice * 2 + 1, x + x_offset, y - 1, x_offset / 2))
            return pos

        posiciones = calcular_posiciones(1, x=0, y=0, x_offset=1)
        etiquetas = nx.get_node_attributes(G, 'label')

        plt.figure(figsize=(6, 4))
        nx.draw(G, pos=posiciones, labels=etiquetas, with_labels=True, 
                node_size=1200, node_color="#4FC3F7", 
                font_size=12, font_weight="bold")
        plt.margins(0.1)
        plt.show()
