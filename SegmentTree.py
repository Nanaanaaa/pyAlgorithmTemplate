# 好用的太慢, 不好用的也不快, 还是cpp吧

from typing import Generic, List, TypeVar

Info = TypeVar("Info")


class SegmentTree(Generic[Info]):
    def __init__(self, size: int = 0, data: List[Info] = None):
        if data is None:
            data = [Info()] * size
        self.n = len(data)
        self.size = 1 << ((self.n - 1).bit_length() if self.n > 0 else 0)
        self.log = self.size.bit_length() - 1 if self.size > 0 else 0
        self.info: List[Info] = [Info()] * (2 * self.size)
        self.info[self.size : self.size + self.n] = data
        for i in range(1, self.size)[::-1]:
            self.pull(i)

    def pull(self, p: int) -> None:
        self.info[p] = self.info[2 * p] + self.info[2 * p + 1]

    def modify(self, p: int, value: Info) -> None:
        p += self.size
        self.info[p] = value
        for i in range(1, 1 + self.log):
            self.pull(p >> i)

    def __getitem__(self, p: int) -> Info:
        return self.info[p + self.size]

    def query(self, l: int, r: int) -> Info:
        if l == r:
            return Info()
        l += self.size
        r += self.size
        res_left = Info()
        res_right = Info()
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

    def __call__(self, l: int, r: int) -> Info:
        return self.query(l, r)

    def max_right(self, l: int, pred) -> int:
        if l == self.n:
            return self.n
        l += self.size
        cur = Info()
        while True:
            while l % 2 == 0:
                l >>= 1
            if not pred(cur + self.info[l]):
                while l < self.size:
                    l <<= 1
                    if pred(cur + self.info[l]):
                        cur = cur + self.info[l]
                        l += 1
                return l - self.size
            cur = cur + self.info[l]
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r: int, pred) -> int:
        if r == 0:
            return 0
        r += self.size
        cur = Info()
        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            if not pred(self.info[r] + cur):
                while r < self.size:
                    r = r << 1 | 1
                    if pred(self.info[r] + cur):
                        cur = self.info[r] + cur
                        r -= 1
                return r + 1 - self.size
            cur = self.info[r] + cur
            if (r & -r) == r:
                break
        return 0


class Info:
    def __init__(self, mx=0):
        self.mx = mx

    def __add__(self, other):
        return Info(max(self.mx, other.mx))
