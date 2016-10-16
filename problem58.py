
# Prime Spirals

from lib.prime2 import MillerRabin, KnownPrimes
from lib.mod_arith import Mod
import math


# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# m->n
# 1->3
# 2->5
# 3->7

# 2m+1=n
# (n-1)/2=m

# n^2-n+1  = 
# n^2-2n+2 = 
# n^2-3n+3 = 

x = 5


# Initialize at inner 3x3 square
n = 3
d = 5
p = 3
while p*100 > d*x:
    n = n + 2
    d = d + 4

    n2 = n**2

    if MillerRabin.is_prime(n2-(n-1)):
        p = p + 1

    if MillerRabin.is_prime(n2-2*(n-1)):
        p = p + 1

    if MillerRabin.is_prime(n2-3*(n-1)):
        p = p + 1

print n


