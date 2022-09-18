import re
import sys


class CLI:
    """
Function argument conventions: 
1. prefix n,s,is,fun denotes number,string,bool,function; 
2. suffix s means list of thing (so names is list of strings)
3. c is a column index (usually)
Misc routines
Handle Settings
"""    
    def __init__(self) -> None:
        ''' Create a `the` variables'''
        self.the = {}
        self.help = " \n\
CSV : summarized csv file \n\
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license\n\
USAGE: lua seen.lua [OPTIONS]\n\
OPTIONS:\n\
-e  --eg        start-up example                      = nothing\n\
-d  --dump      on test failure, exit with stack dump = false\n\
-f  --file      file with csv data                    = ../data/file.csv\n\
-h  --help      show help                             = false\n\
-n  --nums      number of nums to keep                = 512\n\
-s  --seed      random number seed                    = 10019\n\
-S  --sep       feild sep                             = , "
        self.pattern = r"-(\w+)[\s]*--[\s]*(\w+)[\s]*[^=]*[\s]*=[\s]*(.*)"
        re.sub(self.pattern, self.operation, self.help)

    def operation(self, match):
        k = match.group(2)
        x = match.group(3)
        self.the[k] = self.coerce(x)
    '''-- Parse `the` config settings from `help`.'''
    def coerce(self, s):
        def fun(s1):
            if s1 == "true":
                return True
            if s1 == "false":
                return False
            return s1

        try:
            return int(s)
        except:
            return fun(s)
    '''-- Update settings from values on command-line flags. Booleans need no values
 (we just flip the defaults).'''
    def cli(self, t):
        for slot in t:
            v = t[slot]
            v = str(v)
            n = 0
            for x in sys.argv:
                if n == 0:
                    n += 1
                    continue
                if x == "-" + slot[0] or x == "--" + slot:
                    if v == "False":
                        v = "true"
                        t[slot] = self.coerce(v)
                        continue
                    if v == "True":
                        v = "false"
                        t[slot] = self.coerce(v)
                        continue
                    else:
                        v = sys.argv[n + 1]
                    t[slot] = self.coerce(v)
                n += 1
        if t["help"]:
            exit(self.help)
        return t
