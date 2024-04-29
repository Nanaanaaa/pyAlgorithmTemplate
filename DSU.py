class DSU:
    def __init__(self, n):
        self._f = list(range(n))
        self._siz = [1] * n

    def _find(self, x):
        while x != self._f[x]:
            self._f[x] = self._f[self._f[x]]
            x = self._f[x]
        return x

    def __getitem__(self, i):
        return self._find(i)

    def same(self, x, y):
        return self._find(x) == self._find(y)

    def merge(self, x, y, t=True):
        x = self._find(x)
        y = self._find(y)
        if x == y:
            return False
        if t and self._siz[x] < self._siz[y]:
            x, y = y, x
        self._siz[x] += self._siz[y]
        self._f[y] = x
        return True

    def size(self, x):
        return self._siz[self._find(x)]
