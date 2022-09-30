import cli
import config
import sys
sys.path.append("../tests/")

import tests
''' Start up'''
obj = cli.CLI()
the = obj.cli(obj.the)
config.settings = the

"""Print help by default"""
if len(sys.argv) == 1:
    print(obj.help)

if the["eg"] != "nothing":
    tests.runs(the["eg"])
exit(0 if tests.fails==1 else tests.fail)
