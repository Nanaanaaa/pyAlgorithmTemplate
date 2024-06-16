P = 1000000007


class Comb:
    def __init__(self):
        self.n = 0
        self._fac = [1]
        self._invfac = [1]
        self._inv = [1]

    def init(self, m):
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

    def fac(self, m):
        if m < 0:
            return 0
        if m > self.n:
            self.init(2 * m)
        return self._fac[m]

    def invfac(self, m):
        if m < 0:
            return 0
        if m > self.n:
            self.init(2 * m)
        return self._invfac[m]

    def inv(self, m):
        if m < 0:
            return 0
        if m > self.n:
            self.init(2 * m)
        return self._inv[m]

    def binom(self, n, m):
        if n < m or m < 0:
            return 0
        return self.fac(n) * self.invfac(m) % P * self.invfac(n - m) % P

    def perm(self, n, m):
        if n < m or m < 0:
            return 0
        return self.fac(n) * self.invfac(n - m) % P


comb = Comb()
