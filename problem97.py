
# Large non-Mersenne prime

from lib.mod_arith import Mod

p = (Mod(2, 10000000000) ** 7830457) * 28433 + 1

print str(p)
