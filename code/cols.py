import sym
import num
import re


class Cols:
    """
Cols class 


   - Input ==> The class takes a dictionary of header values 
        (key, value) -> (index, header_name)

   - Output ==> The class calculates the following values

        1) all : a dictionary to store all variables
        2) X : a dictionary to store all independent variables
        3) Y : a dictionary to store all dependent variables
        4) klass : a dictionary to store all the variables which are skipped

"""    
    def __init__(self, names) -> None:
        self.names = names if names else {}
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}
        number_x = 1
        number_y = 1
        for c in self.names:
            s = self.names[c]
            if bool(re.match("^[A-Z]{1}.*", s)):
                # print("Num", c,s)
                self.col = num.Num(c, s)
            else:
                # print("Sym", c,s)
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
                
if __name__ == "__main__":
    pass