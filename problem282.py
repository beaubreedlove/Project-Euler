
# INCOMPLETE

# The Ackermann function

from lib.prime2 import MillerRabin, KnownPrimes
from lib.mod_arith import Mod
import math

ackermann_cache = {}

def ackermann(m, n):
    # set up cache as 2d
    if ackermann_cache.get(m) is None:
        ackermann_cache[m] = {}

    # try to get from cache
    if ackermann_cache.get(m).get(n) is not None:
        return ackermann_cache.get(m).get(n)

    result = None

    if m == 0:
        result = n + 1
    elif n == 0:
        result = ackermann(m-1, 1)
    else:
        result = ackermann(m-1, ackermann(m, n-1))

    ackermann_cache[m][n] = result

    return result




for x in xrange(0,4):
    for i in xrange(0,x+1):
        for j in xrange(0,x+1):
            print "A(" + str(i) + "," + str(j) + ") = " + str(ackermann(i,j))

