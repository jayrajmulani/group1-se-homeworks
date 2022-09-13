import num, sym
import re


class Cols:
    def __init__(self, names) -> None:
        self.names = names if names else {}
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}

    def cols(self):
        number_x = 1
        number_y = 1
        for c in self.names:
            s = self.names[c]
            if re.search("^[A-Z]*", s):
                self.col = num.Num(c, s)
            else:
                self.col = sym.Sym(c, s)
            self.all[c] = self.col
            if not ((re.search("[:$]", s))):
                if re.search("[!+-]", s):
                    self.y[number_y] = self.col
                    number_y += 1
                else:
                    self.x[number_x] = self.col
                    number_x += 1
            else:
                self.klass = self.col


#   ONLY FOR TESTING
#
# print(self.all, "x\n",self.x, "y\n",self.y, "klass", self.klass)

# names= {1:       "Clndrs",
# 2 :      "Volume",
# 3  :     "Hp:",
# 4  :     "Lbs-",
# 5 :     "Acc+",
# 6  :     "Model",
# 7  :     "origin",
# 8  :     "Mpg+"}

# c = Cols(names)
# c.cols()
