import config
import traceback
import math


def standard_dev(nums):
    mean = sum(nums) / len(nums)
    std = (sum([((x - mean) ** 2) for x in nums]) / len(nums)) ** 0.5
    return round(std, 2)


def dump_error(e):
    if config.settings["dump"]:
        print("*" * 80)
        traceback.print_exception(e)
        print("*" * 80)


def print_result(message, k, status):
    print(f"\n!!!!!\t{message}\t{k}\t{status}")
    print()

'''Call `fun` on each row. Row cells are divided in `the.seperator`.'''
def csv(fname, fun, sep=None, src=None, s=None, t=None):
    sep = config.settings["sep"].strip()
    with open(fname) as f:
        column_names = [c.strip() for c in f.readline().split(sep)]
        column_indices = list(range(1, len(column_names) + 1))
        columns = dict(zip(column_indices, column_names))
        while True:
            t = {}
            line = f.readline()
            for s in line.split(sep):
                try:
                    s = float(s)
                except:
                    s = None
                t[1 + len(t)] = s
            fun(xs=columns, row=t)
            if not line or len(line.strip()) == 0:
                break


def rnd(x, places):
    if places:
        mult = pow(10, places)
    else:
        mult = pow(10, 2)

    return math.floor(x * mult + 0.5) / mult
