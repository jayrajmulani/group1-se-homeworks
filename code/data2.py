
from utils import *
from cols import *

class data:
    def __init__(self, src=None) -> None:
        self.cols = 0
        self.rows = {}
        if type(src) == "string":
            csv(src,  self.add())
        
        else:
            for row in src.values():
                self.add(row)


    def add(self, xs , row= None):
        if not self.cols :
            self.cols = Cols(xs)
        else :
            row.append(self.row, xs.cells and xs or Row(xs))
            for todo in [self.cols.x, self.cols.y]:
                for col in[todo]:
                    col.add(self,row.cells[col.at])
                
                
    def stats(self,showCols,fun,v, places=None,t= None):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t={}
        for col in [showCols]:
            v=fun(col)
            v=type(v)=="number" and rnd(v,places) or v
            t[col.name]=v 
        return t

            