class Fenwick:
    def __init__(self, data):
        if isinstance(data, int):
            self.n = data
            self.tr = [0] * self.n
        else:
            self.n = len(data)
            self.tr = [0] * self.n
            for i, v in enumerate(data):
                self.add(i, v)

    def add(self, p: int, v: int):
        p += 1
        while p <= self.n:
            self.tr[p - 1] += v
            p += p & -p

    def sum(self, p: int):
        ans = 0
        while p > 0:
            ans += self.tr[p - 1]
            p -= p & -p
        return ans

    def rangeSum(self, l: int, r: int):
        return self.sum(r) - self.sum(l)

    def find(self, k: int):
        x = 0
        cur = 0
        i = 1 << self.n.bit_length()
        while i > 0:
            if x + 1 <= self.n and cur + self.tr[x + i - 1] <= k:
                x += i
                cur += self.tr[x + i - 1]
            i >>= 1
        return x

    def __getitem__(self, x):
        if isinstance(x, int):  # fen[x] => rangeSum(x, x + 1)
            return self.rangeSum(x, x + 1)
        elif isinstance(x, slice):  # fen[l:r] => rangeSum(l, r)
            l, r = x.start, x.stop
            if l is None:
                l = 0
            if r is None:
                r = self.n
            return self.rangeSum(l, r)
        else:
            raise TypeError("__getitem__ type error")

    def __setitem__(self, x, v):  # fen[x] += v => fen.add(x, v)
        if isinstance(x, int):
            self.add(x, v - self[x])
        else:
            raise TypeError("__setitem__ type error")
