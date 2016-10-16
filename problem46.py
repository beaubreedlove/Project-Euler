
# Goldbach's other conjectture

from lib.prime2 import MillerRabin, KnownPrimes
from lib.mod_arith import Mod
import math

def is_prime(n):
    if KnownPrimes.is_prime(n):
        return True

    if KnownPrimes.is_composite(n):
        return False

    if MillerRabin.is_prime(n):
        KnownPrimes.save_prime(n)
        return True
    else:
        KnownPrimes.save_composite(n)
        return False

def satisfies_goldbach(n):
    m = int(math.floor(math.sqrt(n)))

    for i in xrange(0, m + 1):
        if is_prime(n - ((i ** 2) * 2)):
            return True
    return False

o = 3

while satisfies_goldbach(o):
    o = o + 2

print o
