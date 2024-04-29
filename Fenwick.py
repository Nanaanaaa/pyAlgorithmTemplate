class Fenwick:
    class Proxy:
        def __init__(self, fen, idx):
            self.idx = idx
            self.fen = fen

        def add(self, v):
            self.fen.add(self.idx, v)
            return self

    def __init__(self, data):
        if isinstance(data, int):
            self.n = data
            self.tr = [0] * self.n
        else:
            self.n = len(data)
            self.tr = [0] * self.n
            for idx, value in enumerate(data):
                self.add(idx, value)

    def add(self, idx, v):
        idx += 1
        while idx <= self.n:
            self.tr[idx - 1] += v
            idx += idx & -idx

    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.tr[idx - 1]
            idx -= idx & -idx
        return result

    def rangeSum(self, l, r):
        return self.sum(r) - self.sum(l)

    def __getitem__(self, idx):
        return self.Proxy(self, idx)

    def __call__(self, l=None, r=None):
        if l is not None and r is not None:
            return self.rangeSum(l, r)
        elif l is not None:
            return self.sum(l + 1)
        else:
            raise ValueError("Invalid arguments")
