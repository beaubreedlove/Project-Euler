
# The hyperexponentiation of a number

import math
import sys
from lib.mod_arith import Mod

sys.setrecursionlimit(2000)

def hype(a, b):
    if b == 1:
        return a

    return a ** int(hype(a, b - 1))

print hype(Mod(1777, 100000000), 1855)
