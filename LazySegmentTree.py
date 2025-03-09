# 好用的太慢, 不好用的也不快, 还是cpp吧

import sys, math, string
from collections import defaultdict
from bisect import bisect_right as upper_bound, bisect_left as lower_bound

input = lambda: sys.stdin.readline().rstrip()
read = lambda: int(input())
reads = lambda: list(map(int, input().split()))


class LazySegmentTree:
    def __init__(
        self,
        data=None,
        size=0,
        Info=None,
        Tag=None,
    ):
        self.Info = Info
        self.Tag = Tag
        self.infoApply = infoApply
        self.tagApply = tagApply
        self.add = add

        self.n = len(data)
        self.size = 1 << ((self.n - 1).bit_length() if self.n > 0 else 0)
        self.log = self.size.bit_length() - 1 if self.size > 0 else 0

        self.info = [self.Info] * (2 * self.size)
        self.info[self.size : self.size + self.n] = (
            data if data is not None else [Info] * size
        )

        self.tag = [self.Tag] * self.size
        for i in range(self.size - 1, 0, -1):
            self.pull(i)

    def modify(self, p: int, value) -> None:
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)

        self.info[p] = value
        for i in range(1, self.log + 1):
            self.pull(p >> i)

    def __getitem__(self, p: int):
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.info[p]

    def query(self, l: int, r: int):
        if l == r:
            return self.Info
        l += self.size
        r += self.size
        res_left = self.Info
        res_right = self.Info

        for i in range(self.log, 0, -1):
            if (l >> i << i) != l:
                self.push(l >> i)
            if (r >> i << i) != r:
                self.push((r - 1) >> i)

        while l < r:
            if l & 1:
                res_left = self.add(res_left, self.info[l])
                l += 1
            if r & 1:
                r -= 1
                res_right = self.add(self.info[r], res_right)
            l >>= 1
            r >>= 1
        return self.add(res_left, res_right)

    def __call__(self, l: int, r: int):
        return self.query(l, r)

    def rangeApply(self, l: int, r: int, t):
        if l == r:
            return

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if (l >> i << i) != l:
                self.push(l >> i)
            if (r >> i << i) != r:
                self.push((r - 1) >> i)

        x, y = l, r
        while x < y:
            if x & 1:
                self.apply(x, t)
                x += 1
            if y & 1:
                y -= 1
                self.apply(y, t)
            x >>= 1
            y >>= 1

        for i in range(1, self.log + 1):
            if (l >> i << i) != l:
                self.pull(l >> i)
            if (r >> i << i) != r:
                self.pull((r - 1) >> i)

    def maxRight(self, l: int, pred) -> int:
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)

        cur = self.Info

        while True:
            while l % 2 == 0:
                l >>= 1
            if not pred(self.add(cur, self.info[l])):
                while l < self.size:
                    self.push(l)
                    l <<= 1
                    if pred(self.add(cur, self.info[l])):
                        cur = self.add(cur, self.info[l])
                        l += 1
                return l - self.size
            cur = self.add(cur, self.info[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def minLeft(self, r: int, pred) -> int:
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)

        cur = self.Info

        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            if not pred(self.add(self.info[r], cur)):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if pred(self.add(self.info[r], cur)):
                        cur = self.add(self.info[r], cur)
                        r -= 1
                return r + 1 - self.size
            cur = self.add(self.info[r], cur)
            if (r & -r) == r:
                break
        return 0

    def apply(self, p: int, t) -> None:
        self.info[p] = self.infoApply(self.info[p], t)
        if p < self.size:
            self.tag[p] = self.tagApply(self.tag[p], t)

    def pull(self, p: int) -> None:
        self.info[p] = self.add(self.info[2 * p], self.info[2 * p + 1])

    def push(self, p: int) -> None:
        self.apply(2 * p, self.tag[p])
        self.apply(2 * p + 1, self.tag[p])
        self.tag[p] = self.Tag


def tagApply(a, b):
    l_b, l_c = a
    r_b, r_c = b
    return (l_b * r_b % P, (l_c * r_b + r_c) % P)


def infoApply(l, r):
    ans, siz = l
    b, c = r
    return ((ans * b + c * siz) % P, siz)


def add(a, b):
    l_ans, l_siz = a
    r_ans, r_siz = b
    return ((l_ans + r_ans) % P, l_siz + r_siz)


Info = (0, 1)
Tag = (1, 0)
