import config
import traceback


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
