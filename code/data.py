from utils import *
from cols import *
from row import *
import num, sym

class Data:
    def __init__(self, src=None) -> None:
        self.cols = None
        self.rows = {}
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for row in src.values():
                self.add(row)

    def add(self, xs, row=None):
        if not self.cols:
            self.cols = Cols(xs)
            # print("COLS", self.cols)
        else:
            self.rows[1 + len(self.rows)] = xs if "cells" in xs.keys() else Row(xs)
            for _, todo in dict(zip(self.cols.x, self.cols.y)).items():
                for col in [todo]:
                    col.add(self, row.cells[col.at])

    def stats(self,fun, places=2, showCols=None, t=None):
        showCols = self.cols.y if not showCols else showCols
        # fun = mid if not fun else fun
        print(showCols)
        t = {}
        for col in showCols:
            print("CCCC" ,col)
            v = fun(col)
            v = rnd(v, places) if isinstance(v,int) else v
            t[col.name] = v
        return t
