class queue:
    def __init__(self):
        self.q = [None]
        self.capacity = 1
        self._size = 0
        self.head = 0
        self.rear = -1

    __len__ = lambda self: self._size
    __bool__ = lambda self: self._size != 0

    empty = lambda self: self._size == 0
    size = lambda self: self._size
    clear = lambda self: self.__init__()

    front = lambda self: self.q[self.head]
    back = lambda self: self.q[self.rear]

    def resize(self, capacity):
        self.q = (
            self.q[self.head :] + self.q[: self.head] + [None] * (capacity - self._size)
        )
        self.head = 0
        self.rear = self._size - 1
        self.capacity = capacity
        return

    def push(self, x):
        if self._size == self.capacity:
            self.resize(2 * self.capacity)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = x
        self._size += 1
        return

    def pop(self):
        if not self.empty():
            res = self.q[self.head]
            self.head = (self.head + 1) % self.capacity
            self._size -= 1
            return res
        raise IndexError("queue is empty")
