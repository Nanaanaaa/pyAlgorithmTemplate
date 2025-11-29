class DSU:
    def __init__(self, n: int = 0) -> None:
        self.n = n
        self._f = list(range(n))
        self._siz = [1] * n

    def find(self, x: int) -> int:
        while x != self._f[x]:
            self._f[x] = self._f[self._f[x]]
            x = self._f[x]

        return x

    __getitem__ = lambda self, i: self.find(i)
    same = lambda self, x, y: self.find(x) == self.find(y)
    size = lambda self, x: self._siz[self.find(x)]

    def merge(self, x: int, y: int, merge_by_size: bool = True) -> bool:
        x, y = self.find(x), self.find(y)

        if x == y:
            return False

        if merge_by_size and self._siz[x] < self._siz[y]:
            x, y = y, x

        self._siz[x] += self._siz[y]
        self._f[y] = x

        return True

    def groups(self) -> List[List[int]]:
        p = [self.find(i) for i in range(self.n)]

        ans: List[List[int]] = [[] for _ in range(self.n)]
        for i in range(self.n):
            ans[p[i]].append(i)

        return list(filter(lambda r: r, ans))
