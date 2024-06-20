class queue:
    def __init__(self):
        self.q = []
        self.n = 0
        self.hh = 0
        self.tt = -1
    def pop(self):
        assert self.n != 0
        self.hh = (self.hh - 1 + self.n) % self.n
        assert self.hh != self.tt
    def push(self):
        