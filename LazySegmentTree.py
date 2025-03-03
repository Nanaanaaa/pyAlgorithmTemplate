from typing import Generic, List, TypeVar, Callable

Info = TypeVar("Info")
Tag = TypeVar("Tag")


class LazySegmentTree(Generic[Info, Tag]):
    def __init__(self, data: List[Info] = None, size: int = 0):
        if data is None:
            data = [Info()] * size

        self.n = len(data)
        self.size = 1 << ((self.n - 1).bit_length() if self.n > 0 else 0)
        self.log = self.size.bit_length() - 1 if self.size > 0 else 0

        self.info: List[Info] = [Info()] * (2 * self.size)
        self.info[self.size : self.size + self.n] = data

        self.tag = [Tag() for _ in range(self.size)]
        for i in range(self.size - 1, 0, -1):
            self.pull(i)

    def modify(self, p: int, value: Info) -> None:
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)

        self.info[p] = value
        for i in range(1, self.log + 1):
            self.pull(p >> i)

    def __getitem__(self, p: int) -> Info:
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.info[p]

    def query(self, l: int, r: int) -> Info:
        if l == r:
            return Info()
        l += self.size
        r += self.size
        res_left = Info()
        res_right = Info()

        for i in range(self.log, 0, -1):
            if (l >> i << i) != l:
                self.push(l >> i)
            if (r >> i << i) != r:
                self.push((r - 1) >> i)

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

    def rangeApply(self, l: int, r: int, t: Tag) -> None:
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

    def maxRight(self, l: int, pred: Callable[[Info], bool]) -> int:
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)

        cur = Info()

        while True:
            while l % 2 == 0:
                l >>= 1
            if not pred(cur + self.info[l]):
                while l < self.size:
                    self.push(l)
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

    def minLeft(self, r: int, pred: Callable[[Info], bool]) -> int:
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)

        cur = Info()

        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            if not pred(self.info[r] + cur):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if pred(self.info[r] + cur):
                        cur = self.info[r] + cur
                        r -= 1
                return r + 1 - self.size
            cur = self.info[r] + cur
            if (r & -r) == r:
                break
        return 0

    def apply(self, p: int, t: Tag) -> None:
        self.info[p].apply(t)
        if p < self.size:
            self.tag[p].apply(t)

    def pull(self, p: int) -> None:
        self.info[p] = self.info[2 * p] + self.info[2 * p + 1]

    def push(self, p: int) -> None:
        self.apply(2 * p, self.tag[p])
        self.apply(2 * p + 1, self.tag[p])
        self.tag[p] = Tag()


class Tag:
    def __init__(self) -> None:
        pass

    def apply(self, t: Tag) -> None:
        pass


class Info:
    def __init__(self, ans: int = 0) -> None:
        pass

    def apply(self, t: Tag) -> None:
        pass

    def __add__(self, other: Info) -> None:
        return Info()
