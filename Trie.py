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


class Trie:
    V = 31
    __slots__ = "trie", "tot", "cnt"

    def __init__(self, capacity):
        capacity = capacity * self.V + 2
        self.trie = List(capacity, 2, -1)
        self.tot = 0
        pass

    def newNode(self):
        self.tot += 1
        return self.tot

    def add(self, value):
        o = 0
        for i in range(self.V, -1, -1):
            d = value >> i & 1
            if self.trie[o, d] == -1:
                self.trie[o, d] = self.newNode()
            o = self.trie[o, d]

    def query(self, value):
        ans = 0
        o = 0
        for i in range(self.V, -1, -1):
            d = value >> i & 1
            if self.trie[o, d ^ 1] != -1:
                ans |= 1 << i
                d ^= 1
            o = self.trie[o, d]
        return ans
