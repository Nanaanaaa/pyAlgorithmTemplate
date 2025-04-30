class List(list):
    def __init__(self, n=0, m=0, init=0):
        super().__init__([init] * (n * m))
        self.n = n
        self.m = m

    def __getitem__(self, indices):
        if isinstance(indices, tuple) and len(indices) == 2:
            x, y = indices
            return super().__getitem__(x * self.m + y)
        return super().__getitem__(indices)

    def __setitem__(self, indices, value):
        if isinstance(indices, tuple) and len(indices) == 2:
            x, y = indices
            super().__setitem__(x * self.m + y, value)
        else:
            super().__setitem__(indices, value)

    def __iadd__(self, value):
        for i in range(len(self)):
            self[i] += value
        return self

    def __isub__(self, value):
        for i in range(len(self)):
            self[i] -= value
        return self

    def __str__(self):
        result = []
        for i in range(self.n):
            result.append(str(self[i * self.m : (i + 1) * self.m]))
        return "\n".join(result)
