# INCOMPLETE

# Primes with runs

# Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:

# 1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

# We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

# So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

# In the same way we obtain the following results for 4-digit primes.

# Digit, d    M(4, d) N(4, d) S(4, d)
# 0   2   13  67061
# 1   3   9   22275
# 2   3   1   2221
# 3   3   12  46214
# 4   3   2   8888
# 5   3   1   5557
# 6   3   1   6661
# 7   3   9   57863
# 8   3   1   8887
# 9   3   7   48073
# For d = 0 to 9, the sum of all S(4, d) is 273700.

# Find the sum of all S(10, d).

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

def debug(s):
    print str(s)
    pass

def MNS(n, d):
    M = n
    N = 0
    S = 0

    debug("While M from " + str(n) + " to 0")
    while M >= 0:
        debug("\tM = " + str(M))
        other_digits = n - M
        mid_section = math.floor((10 ** M)/9) * d

        debug("\tWhile after_digits from 0 to " + str(other_digits))
        after_digits = 0
        while after_digits <= other_digits:
            debug("\t\tafter_digits = " + str(after_digits))
            before_digits = n - M - after_digits
            debug("\t\tbefore_digits = " + str(before_digits))
            debug("\t\tWhile after from 0 to " + str(10 ** after_digits))
            after = 0
            while after < 10 ** after_digits:
                debug("\t\t\tafter = " + str(after))
                debug("\t\t\tWhile before from 0 to " + str(10 ** before_digits))
                before = 0
                while before < 10 ** before_digits:
                    debug("\t\t\t\tbefore = " + str(before))
                    debug("piece a = " + str(before * (10 ** (M + before_digits))))
                    debug("piece b = " + str(mid_section * (10 ** d)))
                    debug("piece c = " + str(after))
                    x = int(before * (10 ** (M + after_digits)) + mid_section * (10 ** after_digits) + after)
                    debug("\t\t\t\tx = " + str(x))
                    if is_prime(x):
                        debug("PRIME --> " + str(x))
                        N = N + 1
                        S = S + x
                    before = before + 1
                after = after + 1

            after_digits = after_digits + 1

        if N > 0:
            return (M,N,S)

        M = M - 1

print str(MNS(4,1))

