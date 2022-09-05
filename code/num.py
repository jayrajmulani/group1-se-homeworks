from utils import *
import sys
import random
from config import *
import statistics


class Num:
    def __init__(self, c=None, s=None) -> None:
        self.n = 0
        self.at = c if c else 0
        self.name = s if s else ""
        self._has = []
        self.isSorted = True
        self.lo = sys.maxsize
        self.high = -sys.maxsize - 1
        self.w = -1 if s and "-" in s else 1

    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted = True
        return self._has

    def add(self, v, pos=None):
        if v != "?":
            self.n = self.n + 1
            v = int(v)
            self.lo = min(v, self.lo)
            self.high = max(v, self.high)
            if len(self._has) < settings["nums"]:
                self._has.append(v)
            else:
                pos = int(random.random() * 100) % len(self._has)
                self._has[pos] = v

            self.isSorted = False

    def div(self, a=None):
        if not a:
            a = self._has
        # return standard_dev(a)
        return statistics.stdev(a)

    def mid(self, a=None):
        if not a:
            a = self.nums()
        n = len(a)
        if n % 2 == 0:
            median = (a[n // 2] + a[n // 2 - 1]) / 2
        else:
            median = a[n // 2]
        return median
