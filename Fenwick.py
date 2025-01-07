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
