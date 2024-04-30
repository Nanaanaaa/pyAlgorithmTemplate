import heapq


class priority_queue:
    def __init__(self):
        self._pq = []

    def push(self, item):
        return heapq.heappush(self._pq, -item)

    def pop(self):
        return -heapq.heappop(self._pq)

    def top(self):
        return -self._pq[0][-1]

    def empty(self):
        return len(self._pq) == 0

    def size(self):
        return len(self._pq)
