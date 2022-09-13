import config
import traceback
import cli
import math


def standard_dev(nums):
    mean = sum(nums) / len(nums)
    std = (sum([((x - mean) ** 2) for x in nums]) / len(nums)) ** 0.5
    return std


def dump_error(e):
    if config.settings["dump"]:
        print("*" * 80)
        traceback.print_exception(e)
        print("*" * 80)


def print_result(message, k, status):
    print(f"\n!!!!!\t{message}\t{k}\t{status}")
    print()


def csv(fname, fun, sep=None, src=None, s=None, t=None):
    sep = config.settings["sep"]
    with open(fname) as src:
        while s := src.readline().rstrip():
            t = {}
            for s1 in s.split(sep):
                t[1 + len(t)] = cli.CLI.coerce(s1)

            fun(t)


def copy(t, u):
    if type(t) != "table":
        return t
    u = {}
    for k, v in u.iteritems():
        u[k] = copy(v)
    return setmetatable(u, getmetatable(t))


def rnd(x, places):
    if places:
        mult = pow(10, places)
    else:
        mult = pow(10, 2)

    return math.floor(x * mult + 0.5) / mult
