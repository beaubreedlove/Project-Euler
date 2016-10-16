
# The hyperexponentiation of a number

import math
from lib.mod_arith import Mod

M = 10 ** 10

total = Mod(0, M)

for i in xrange(1, 1000 + 1):
    total = total + Mod(i, M) ** i

print total
