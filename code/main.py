import cli
import config
import num
import random

obj = cli.CLI()
the = obj.cli(obj.the)
config.settings["nums"] = obj.the['nums']
print(obj.the)

def populate_num():
    n = num.Num()
    for i in range(1, 1001):
        n.add(random.randint(1,i+1))
    print(n.nums())
    print(len(n._has))


populate_num()