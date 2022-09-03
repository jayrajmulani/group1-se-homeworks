from distutils.command.config import config
from utils import *
import sys
import random
from config import *


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

    def add(self,v ,pos):
        if v!="?":
            self.n = self.n + 1
            v = int(v)
            self.lo = min(v, self.lo)
            self.high = max(v, self.high)
            if len(self._has) < settings["nums"]:
                self._has.append(v)
            
            elif random.randint(0,len(self._has)) < (settings["nums"]/self.n):
                pos = random.randint(0,len(self._has))
                self._has[pos] = v
            
            self.isSorted = False


    def div(self,a=None):
        
        if not a : a = self._has
        return standard_dev(a)
            




