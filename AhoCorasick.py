class AhoCorasick:
    def __init__(self, A=26):
        self.A = A
        self.t = []
        self.init()

    class Node:
        def __init__(self, ahoCorasick):
            self.len = 0
            self.link = 0
            self.cnt = 0
            self.vis = False
            self.next = [0] * ahoCorasick.A

        def __getitem__(self, x):
            return self.next[x]

        def __setitem__(self, x, value):
            self.next[x] = value

    def init(self):
        self.t = [self.Node(self), self.Node(self)]
        self.t[0].next = [1] * self.A
        self.t[0].len = -1

    def new_node(self):
        self.t.append(self.Node(self))
        return len(self.t) - 1

    def add(self, a, offset="a"):
        if isinstance(a, str):
            a = [ord(c) - ord(offset) for c in a]
        p = 1
        for x in a:
            if self.t[p][x] == 0:
                self.t[p][x] = self.new_node()
                self.t[self.t[p][x]].len = self.t[p].len + 1
            p = self.t[p][x]
        self.t[p].cnt += 1
        return p

    def work(self):
        q = [1]
        for i in range(len(q)):
            x = q[i]
            for j in range(self.A):
                if self.t[x][j] == 0:
                    self.t[x][j] = self.t[self.t[x].link][j]
                else:
                    self.t[self.t[x][j]].link = self.t[self.t[x].link][j]
                    q.append(self.t[x][j])

    def next(self, p, x, offset="a"):
        if isinstance(x, str):
            x = ord(x) - ord(offset)
        return self.t[p][x]

    def link(self, p):
        return self.t[p].link

    def length(self, p):
        return self.t[p].len

    def size(self):
        return len(self.t)
