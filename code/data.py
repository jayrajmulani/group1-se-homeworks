from utils import *
from cols import *
from row import *


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
            print("COLS", self.cols)
        else:
            self.rows[1 + len(self.rows)] = xs if "cells" in xs.keys() else Row(xs)
            for _, todo in [self.cols.x, self.cols.y]:
                for col in [todo]:
                    col.add(self, row.cells[col.at])

    def stats(self, showCols, fun, v, places=None, t=None):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t = {}
        for col in [showCols]:
            v = fun(col)
            v = type(v) == "number" and rnd(v, places) or v
            t[col.name] = v
        return t
