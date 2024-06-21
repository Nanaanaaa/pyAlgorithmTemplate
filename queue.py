class queue:
    def __init__(self):
        self.q = [None]
        self.capacity = 1
        self.siz = 0
        self.head = 0
        self.rear = -1

    def empty(self):
        return self.siz == 0

    def size(self):
        return self.siz

    def resize(self, capacity):
        q = [None] * capacity
        for i in range(self.siz):
            q[i] = self.q[(self.head + i) % self.capacity]
        self.q = q
        self.front = 0
        self.rear = self.siz - 1
        self.capacity = capacity
        return

    def push(self, x):
        if self.siz == self.capacity:
            self.resize(2 * self.capacity)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = x
        self.siz += 1
        return

    def pop(self):
        if not self.empty():
            res = self.q[self.head]
            self.head = (self.head + 1) % self.capacity
            self.siz -= 1
            return res
        raise IndexError("queue is empty")

    def front(self):
        return self.q[self.head]

    def back(self):
        return self.q[self.rear]
