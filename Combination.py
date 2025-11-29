P = 1000000007


class Comb:
    def __init__(self) -> None:
        self.n = 0
        self._fac = [1]
        self._invfac = [1]
        self._inv = [1]

    def init(self, m: int) -> None:
        m = min(m, P - 1)
        if m <= self.n:
            return

        self._fac += [1] * (m - self.n)
        self._invfac += [1] * (m - self.n)
        self._inv += [1] * (m - self.n)

        for i in range(self.n + 1, m + 1):
            self._fac[i] = self._fac[i - 1] * i % P

        self._invfac[m] = pow(self._fac[m], P - 2, P)

        for i in range(m, self.n, -1):
            self._invfac[i - 1] = self._invfac[i] * i % P
            self._inv[i] = self._invfac[i] * self._fac[i - 1] % P

        self.n = m

    def fac(self, m: int) -> int:
        if m > self.n:
            self.init(2 * m)
        return 0 if m < 0 else self._fac[m]

    def invfac(self, m: int) -> int:
        if m > self.n:
            self.init(2 * m)
        return 0 if m < 0 else self._invfac[m]

    def inv(self, m: int) -> int:
        if m > self.n:
            self.init(2 * m)
        return 0 if m < 0 else self._inv[m]

    binom = lambda self, n, m: (
        0
        if n < m or m < 0
        else self.fac(n) * self.invfac(m) % P * self.invfac(n - m) % P
    )
    perm = lambda self, n, m: (
        0 if n < m or m < 0 else self.fac(n) * self.invfac(n - m) % P
    )


comb = Comb()
