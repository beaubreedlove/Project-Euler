
import math
from random import random
from mod_arith import Mod


class KnownPrimes:
    # We know the primality of all positive integers <= this value
    known_consecutive_primes_upper_bound = 6
    known_consecutive_primes = {
        2: True,
        3: True,
        5: True,
    }

    # todo: try some other blist data structures
    known_primes = {}
    known_composites = {}

    @staticmethod
    def is_prime(n):
        return n in KnownPrimes.known_consecutive_primes or n in KnownPrimes.known_primes

    @staticmethod
    def is_composite(n):
        if n <= KnownPrimes.known_consecutive_primes_upper_bound:
            return n not in KnownPrimes.known_consecutive_primes

        return n in KnownPrimes.known_composites

    @staticmethod
    def save_primes(primes):
        for p in primes:
            KnownPrimes.save_prime(p)

    @staticmethod
    def save_prime(prime):
        if (prime > KnownPrimes.known_consecutive_primes_upper_bound):
            KnownPrimes.known_primes[prime] = True

    @staticmethod
    def save_consecutive_primes(consecutive_primes, upper_bound=None):
        m = KnownPrimes.known_consecutive_primes_upper_bound

        if upper_bound is not None:
            m = max(m, upper_bound)

        for p in consecutive_primes:
            KnownPrimes.known_consecutive_primes[p] = True
            m = max(m, p)

        KnownPrimes.known_consecutive_primes_upper_bound = m

    def save_composites(composites):
        for c in composites:
            KnownPrimes.save_composite(c)

    @staticmethod
    def save_composite(composite):
        if (composite > KnownPrimes.known_consecutive_primes_upper_bound):
            KnownPrimes.known_composites[composite] = True


class MillerRabin:

    @staticmethod
    def is_prime(n, k=None):
        if n < 2 or n % 2 == 0:
            return n == 2

        # write n-1 as 2^s*d
        d = n-1
        s = 0
        while d % 2 == 0:
            d = d / 2
            s = s + 1

        for a in MillerRabin.get_a_range(n, k):
            if Mod(a, n) ** d != 1:
                all_pass = True
                for r in xrange(0, s):
                    if Mod(a, n) ** ((2**r) * d) == -1:
                        all_pass = False
                        break
                if all_pass:
                    return False

        return True

    @staticmethod
    def get_a_range(n, k=None):
        if n < 2047:
            for a in [2]:
                yield a
        elif n < 1373653:
            for a in [2, 3]:
                yield a
        elif n < 9080191:
            for a in [31, 37]:
                yield a
        elif n < 25326001:
            for a in [2, 3, 5]:
                yield a
        elif n < 4759123141:
            for a in [2, 7, 61]:
                yield a
        elif n < 1122004669633:
            for a in [2, 13, 23, 1662803]:
                yield a
        elif n < 2152302898747:
            for a in [2, 3, 5, 7, 11]:
                yield a
        elif n < 3474749660383:
            for a in [2, 3, 5, 7, 11, 13]:
                yield a
        elif n < 341550071728321:
            for a in [2, 3, 5, 7, 11, 13, 17]:
                yield a
        elif n < 3825123056546413051:
            for a in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
                yield a
        elif n < 18446744073709551616: # 2^64
            for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
                yield a
        elif n < 318665857834031151167461:
            for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
                yield a
        elif n < 3317044064679887385961981 or True:
            for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
                yield a
        else:
            max_a = min(n-1,int(math.floor(2*(math.log(n))**2)))
            print "MillerRabin.get_a_range() resorted to enumerating over 2 < a < " + str(max_a)
            if k is None:
                a = 2
                while a <= max_a:
                    yield a
                    a = a + 1
            else:
                print "Only testing a limited number of `a` values. Results will not be guarenteed!"
                while k > 0:
                    a = math.floor(2+random()*(max_a-1)) # random int from 2 through max_a
                    yield a
                    k = k - 1










