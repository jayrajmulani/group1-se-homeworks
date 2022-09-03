import sys


class Num:
    def __init__(self, c, s) -> None:
        self.n = 0
        self.at = c if c else 0
        self.name = s if s else ""
        self._has = []
        self.isSorted = True
        self.lo = sys.maxint
        self.high = sys.minint
        self.w = -1 if "-" in s else 1

    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted = True
        return self._has
