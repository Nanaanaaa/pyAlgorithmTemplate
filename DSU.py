class DSU:
    def __init__(self, n):
        self.n = n
        self._f = list(range(n))
        self._siz = [1] * n

    def find(self, x):
        while x != self._f[x]:
            self._f[x] = self._f[self._f[x]]
            x = self._f[x]
        return x

    def __getitem__(self, i):
        return self.find(i)

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y, t=True):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if t and self._siz[x] < self._siz[y]:
            x, y = y, x
        self._siz[x] += self._siz[y]
        self._f[y] = x
        return True

    def size(self, x):
        return self._siz[self.find(x)]

    def group(self):
        p = [self.find(i) for i in range(self.n)]
        ans = [[] for _ in range(self.n)]
        for i in range(self.n):
            ans[p[i]].append(i)
        return [i for i in ans if len(i) != 0]
