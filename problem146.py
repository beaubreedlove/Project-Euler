
# Investigating a prime pattern

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

x = 150000000
are_prime = [1,3,7,9,13,27]
arent_prime = [15, 17, 19, 21, 23, 25]

# all primes are 
# 1, 7, 11, 13, 17, 19, 23 or 29 mod 30
# thus i^2 = 10 mod 30 is the only that can get a prime in this pattern
# this i = 10 or 20 mod 30

total = 0
i = 10
while i < x:
    if i % 100000 == 0:
        print "i = " + str(i)
    s = i**2
    passed = True
    for j in are_prime:
        if not is_prime(s+j):
            passed = False
            break

    if passed:
        for j in arent_prime:
            if is_prime(s+j):
                passed = False
                break

        if passed:
            print "i^2 = " + str(i) + "^2 = " + str(s)
            total = total + i

    if i % 3 == 1:
        # i = 10 mod 30
        i = i + 10
    else:
        # i = 20 mod 30
        i = i + 20

print total

