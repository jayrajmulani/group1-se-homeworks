from config import *
from cli import *

def standard_dev(nums):
    mean = sum(nums) / len(nums)
    std = (sum([((x - mean) ** 2) for x in nums]) / len(nums))** 0.5
    return std


def csv(fname, fun, sep=None,src=None,s=None,t=None):
    sep = settings["sep"]
    with open(fname) as src:
        while(s := src.readline().rstrip()):
            t = {}
            for s1 in s.split(sep):
                t[1 + len(t)] = CLI.coerce(s1)

            fun(t)


   

