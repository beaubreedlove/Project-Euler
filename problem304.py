
# Primonacci

from lib.prime2 import MillerRabin, KnownPrimes
from lib.mod_arith import Mod
from math import *

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

def next_prime(n):
    for n in xrange(n, 2 * n):
        if is_prime(n):
            return n
    raise "next_prime assumption failed"

def a(n):
    if n == 1:
        return next_prime(10**14)
    return next_prime(a(n-1))

PHI = (sqrt(5)-1)/2+1

def f(n):
    return (P ** n - (-P) **(-n))/sqrt(5)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return f(n-1) + f(n-2)

def b(n):
    return f(a(n))

result = Mod(0, 1234567891011)

for n in xrange(1, 100000 + 1):
    result = result + b(n)

print result
