import utils


class row:
    def __init__(self, t):
        return {"cells": t, "cooked": utils.copy(t), "isEvaled": False}
