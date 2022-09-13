import config
import traceback
import cli
import math
import copy


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
    print(config.settings)
    sep = config.settings["sep"]
    with open(fname) as src:
        while s := src.readline().rstrip():
            t = {}
            for s1 in s.split(sep):
                print(s1)
                try:
                    t[1 + len(t)] = cli.CLI.coerce(s1)
                except:
                    pass
            fun(t)


def rnd(x, places):
    if places:
        mult = pow(10, places)
    else:
        mult = pow(10, 2)

    return math.floor(x * mult + 0.5) / mult
