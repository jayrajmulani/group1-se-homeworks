import math


class Sym:
    def __init__(self, c=None, s=None) -> None:
        self.n = 0
        self.at = c if c else 0
        self.name = s if s else ""
        self._has = {}

    def add(self, v):
        if v != "?":
            self.n = self.n + 1
            if v in self._has:
                self._has[v] += 1
            else:
                self._has[v] = 1

    def mid(self, col=None, mode=None, most=None):
        most = -1
        for k, v in self._has.items():
            if v > most:
                mode = k
                most = v
        return mode

    def div(self, e=None):
        def func(p):
            return p * (math.log(p, 2))

        e = 0
        for _, i in self._has.items():
            if i > 0:
                e = e - func(i / self.n)
        return e
