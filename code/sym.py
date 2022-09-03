import math


class Sym:
    def Sym_add(self):
        C.append((input("Enter a char"))[0])

    def calculate_mode(self):
        print("Mode of List C is % s" % (max(set(C), key=C.count)))

    def calculate_entropy(self):
        en = 0
        for i in P:
            en = en + i*(math.log2(i))
        en = en*(-1)
        print("Entropy is", en)


C = ['@', '#', '#', '%', '*']
P = [0.1, 2, 5, 0.23, 3]

s1 = Sym()
s1.Sym_add()
s1.calculate_mode()
s1.calculate_entropy()
