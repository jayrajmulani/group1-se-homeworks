import copy


class Row:
    def __init__(self, t):
        self.cells = t
        self.cooked = copy.deepcopy(t)
        self.isEvaled = False
