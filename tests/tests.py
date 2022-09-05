import sys

sys.path.append("../code/")

import num, sym, cli, main, config


def test_the():
    assert True


def test_sym():
    s = sym.Sym()
    for c in ["a", "a", "a", "a", "b", "b", "c"]:
        s.add(c)
    mode, entropy = s.mid(), s.div()
    entropy = (1000 * entropy) // 1 / 1000
    assert mode == "a" and 1.37 <= entropy and entropy <= 1.38


def test_num():
    n = num.Num()
    config.settings["nums"] = 100
    for i in range(1, 101):
        n.add(i)
    print(n.nums())
    mid, div = n.mid(), n.div()
    print(mid, div)
    assert 50 <= mid and mid <= 52 and 29 < div and div < 31


def test_bignum():
    n = num.Num()
    config.settings["nums"] = 32
    for i in range(1, 1001):
        n.add(i)
    print(n.nums())
    assert len(n._has) == 32


# print(cli.a)
