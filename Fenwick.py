class Fenwick:
    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, v: int) -> None:
        p += 1
        while p <= self._n:
            self.data[p - 1] += v
            p += p & -p

    def sum(self, p: int):
        ans = 0
        while p > 0:
            ans += self.data[p - 1]
            p -= p & -p

        return ans

    def rangeSum(self, l: int, r: int):
        return self.sum(r) - self.sum(l)

    def find(self, k: int):
        x = 0
        cur = 0
        i = 1 << self._n.bit_length()
        while i > 0:
            if x + 1 <= self._n and cur + self.data[x + i - 1] <= k:
                x += i
                cur += self.data[x + i - 1]
            i >>= 1

        return x

    def __getitem__(self, x):
        if isinstance(x, int):  # fen[x] => rangeSum(x, x + 1)
            return self.rangeSum(x, x + 1)
        elif isinstance(x, slice):  # fen[l:r] => rangeSum(l, r)
            l = 0 if x.start is None else x.start
            r = self._n if x.stop is None else x.stop
            return self.rangeSum(l, r)
        else:
            raise TypeError("__getitem__ type error")

    def __setitem__(self, x, v):  # fen[x] += v => fen.add(x, v)
        if isinstance(x, int):
            self.add(x, v - self[x])
        else:
            raise TypeError("__setitem__ type error")
