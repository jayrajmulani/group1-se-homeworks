import cli
import config
import sys

sys.path.append("../tests/")

import tests

"""Start up the program - Command Line Interface"""
obj = cli.CLI()
the = obj.cli(obj.the)
config.settings = the

"""Print help if no args provided in the command"""
if len(sys.argv) == 1:
    print(obj.help)

if the["eg"] != "nothing":
    tests.runs(the["eg"])
exit(0)
