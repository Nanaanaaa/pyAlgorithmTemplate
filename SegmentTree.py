from dataclasses import dataclass, field
from math import ceil, log2
from typing import List, Callable, TypeVar, Generic

T = TypeVar("T")


class SegmentTree(Generic[T]):
    def __init__(self, n=0, data: List[T] = None):
        if n != 0:
            data = [Info()] * n
        if data is None:
            data = []
        self.n = len(data)
        if self.n == 0:
            self.size = 1
        else:
            self.size = 1 << ceil(log2(self.n)) if self.n > 0 else 1
        self.log = self.size.bit_length() - 1
        self.info: List[T] = [Info()] * (2 * self.size)

        for i in range(self.n):
            self.info[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.pull(i)

    def pull(self, p: int):
        self.info[p] = self.info[2 * p] + self.info[2 * p + 1]

    def modify(self, p: int, value: T):
        p += self.size
        self.info[p] = value
        for i in range(1, self.log + 1):
            self.pull(p >> i)

    def __getitem__(self, p: int) -> T:
        return self.info[p + self.size]

    def rangeQuery(self, l: int, r: int) -> T:
        if l == r:
            return Info()

        res_left = Info()
        res_right = Info()
        l += self.size
        r += self.size

        while l < r:
            if l & 1:
                res_left = res_left + self.info[l]
                l += 1
            if r & 1:
                r -= 1
                res_right = self.info[r] + res_right
            l >>= 1
            r >>= 1
        return res_left + res_right


INF = 10**9


@dataclass
class Info:
    mxadd: int = -INF
    mnadd: int = INF
    mxdel: int = -INF
    mndel: int = INF
    ans: int = 0

    def __add__(self, other):
        res = Info()
        res.mxadd = max(self.mxadd, other.mxadd)
        res.mnadd = min(self.mnadd, other.mnadd)
        res.mxdel = max(self.mxdel, other.mxdel)
        res.mndel = min(self.mndel, other.mndel)
        res.ans = max(
            self.ans, other.ans, self.mxadd - other.mnadd, other.mxdel - self.mndel
        )
        return res
