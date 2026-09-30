class UnsortedTableMap:

    def __init__(self):
        # Crea un diccionario vacío.
        self._table = []                  # lista de entradas [clave, valor]

    # ---------- auxiliar ----------
    def _buscar(self, k):
        # Retorna el índice de la entrada con clave k, o -1 si no existe.
        for j in range(len(self._table)):
            if self._table[j][0] == k:
                return j
        return -1

    # ---------- núcleo: métodos especiales ----------
    def __len__(self):
        # len(M)
        return len(self._table)

    def __getitem__(self, k):
        # M[k]  (KeyError si no existe)
        j = self._buscar(k)
        if j == -1:
            raise KeyError(k)
        return self._table[j][1]

    def __setitem__(self, k, v):
        # M[k] = v  (inserta o reemplaza)
        j = self._buscar(k)
        if j == -1:
            self._table.append([k, v])
        else:
            self._table[j][1] = v

    def __delitem__(self, k):
        j = self._buscar(k)
        if j == -1:
            raise KeyError(k)
        self._table.pop(j)

    def __contains__(self, k):
        # k in M
        return self._buscar(k) != -1

    def __iter__(self):
        # for k in M  (genera las claves)
        for entrada in self._table:
            yield entrada[0]

    def __eq__(self, otro):
        # M == otro  (mismos pares, sin importar el orden)
        if len(self) != len(otro):
            return False
        for k in self:
            if k not in otro:
                return False
            if self[k] != otro[k]:
                return False
        return True

    def __repr__(self):
        return '{' + ', '.join(f'{k!r}: {v!r}' for k, v in self._table) + '}'
