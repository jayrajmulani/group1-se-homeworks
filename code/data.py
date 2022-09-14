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
        else:
            r = Row(row)
            self.rows[1 + len(self.rows)] = r
            for todo in list(self.cols.x.values()) +list(self.cols.y.values()) :
                try:
                    to_add =  r.cells[todo.at]
                    if to_add:
                        todo.add(to_add)
                except Exception:
                    pass
                    # print("AT", todo.at)
                    # print(r.cells)
                    # print(str(e))
            
    def stats(self,fun, places=2, showCols=None, t=None):
        showCols = self.cols.x if not showCols else showCols
        t = {}
        for k,v in showCols.items():
            if isinstance(v,num.Num):
                fun_to_call = num.Num.mid if fun == "mid" else num.Num.div
            else:
                fun_to_call = sym.Sym.mid if fun == "mid" else sym.Sym.div
            if len(v._has) > 0:
                stat = fun_to_call(v)
                stat = rnd(stat, places) if isinstance(stat,float) else stat
                t[v.name] = stat
        return t
