import heapq


class MinHeap:
    def __init__(self):
        self._pq = []
        return

    def push(self, item):
        return heapq.heappush(self._pq, item)

    def pop(self):
        return heapq.heappop(self._pq)

    def top(self):
        return self._pq[0][-1]

    def empty(self):
        return len(self._pq) == 0

    def size(self):
        return len(self._pq)

    def __bool__(self):
        return not self.empty()
