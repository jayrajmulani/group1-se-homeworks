import sys
import traceback
import utils

sys.path.append("../code/")

import num, sym, config, utils, data

eg = {}
fails = 0


def test_the():
    print("-" * 50)
    return True, "PASS"


def test_sym():
    print("-" * 50)
    s = sym.Sym()
    for c in ["a", "a", "a", "a", "b", "b", "c"]:
        s.add(c)
    mode, entropy = s.mid(), s.div()
    entropy = (1000 * entropy) // 1 / 1000
    print("{ " + f"mid: {mode}, div: {entropy}" + " }")
    status = "PASS" if mode == "a" and 1.37 <= entropy and entropy <= 1.38 else "FAIL"
    return True, status


def test_num():
    print("-" * 50)
    n = num.Num(capacity=100)
    for i in range(1, 101):
        n.add(i)
    mid, div = n.mid(), n.div()
    print("{ " + f"mid: {mid}, div: {div}" + " }")
    status = "PASS" if 50 <= mid and mid <= 52 and 28 < div and div < 30 else "FAIL"
    return True, status


def test_bignum():
    print("-" * 50)
    n = num.Num(capacity=32)
    for i in range(1, 1001):
        n.add(i)
    status = "PASS" if len(n._has) == 32 else "FAIL"
    print(n.nums())
    return True, status


def runs(k):
    try:
        old_settings = config.settings
        if not eg[k]:
            return False
        status, message = eg[k]()
        if k == "LIST":
            message = "PASS"
        utils.print_result(message, k, status)
        config.settings = old_settings
    except Exception as e:
        utils.dump_error(e)
        utils.print_result("CRASH", k, False)
    return status


def bad():
    print("-" * 50)
    try:
        print(eg["someting"]["that"]["doesn't"]["exist!"])
        return True, "PASS"
    except Exception as e:
        utils.dump_error(e)
        return False, "CRASH"


def all():
    global fails
    for k in list()[1]:
        if k != "ALL":
            if not runs(k):
                fails += 1
    print(config.settings)
    return True, "PASS"


def list():
    print("-" * 50)
    return True, sorted(eg.keys())


def ls():
    print("\nExamples of python3 main.py -e...")
    for k in list()[1]:
        print(f"\t{k}")
    return True, "PASS"


def test_data():
    print("-" * 50)
    d = data.Data("../data/file.csv")
    for _, col in d.cols.y.items():
        if not isinstance(col, num.Num):
            continue
        print(
            "{ "
            + f":at {col.at} :hi {col.high} :isSorted {col.isSorted} :lo {col.lo} :n {col.n} :name {col.name} :w {col.w}"
            + " }"
        )
    return True, "PASS"


def test_csv():
    print("{", end=" ")
    d = data.Data("../data/file.csv")
    for i, col in d.cols.all.items():
        print(col.name, end=" ")
    print("}")
    for i, row in d.rows.items():
        if i > 10:
            break
        print("{", end=" ")
        for j, cell in row.cells.items():
            print(cell, end=" ")
        print("}")

    # print(len(d.rows))

    return True, "PASS"


def test_stats():
    d = data.Data("../data/file.csv")
    print()
    print("xmid", d.stats(fun="mid", places=2, showCols=d.cols.x))
    print("xdiv", d.stats(fun="div", places=3, showCols=d.cols.x))
    print("ymid", d.stats(fun="mid", places=2, showCols=d.cols.y))
    print("ydiv", d.stats(fun="div", places=3, showCols=d.cols.y))
    return True, "PASS"


eg["BAD"] = bad
eg["ALL"] = all
eg["LIST"] = list
eg["LS"] = ls
eg["bignum"] = test_bignum
eg["csv"] = test_csv
eg["data"] = test_data
eg["num"] = test_num
eg["stats"] = test_stats
eg["the"] = test_the
eg["sym"] = test_sym
fails = 0
