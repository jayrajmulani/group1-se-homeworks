
from utils import csv


class data:
    def __init__(self, src=None) -> None:
        self.cols = 0
        self.rows = {}
        if type(src) == "string":
            csv(src,  self.add())
        
        else:
            for row in src.values():
                self.add(row)


    def add(self,xs, row=None):
        print("row")

            