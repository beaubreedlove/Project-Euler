
import math
from modulo import Modulo

# Used in problem 3, 7

class Prime:
    # These are consecutive
    # If a prime is known outside the consecutive range, it won't be added
    known_primes = []
    known_composites = [1]

    iter = None

    def is_prime(self, n):
        if n in Prime.known_primes:
            return True

        if n in Prime.known_composites:
            return False

        # this could be improved with an int sqrt algorithm - no need to have a float
        limit = int(math.sqrt(n))

        for i in xrange(2, limit + 1):
            if self.is_prime(i):
                if n % i == 0:
                    Prime.known_composites.append(n)
                    return False

        Prime.known_primes.append(n)
        return True

    def primes_up_to(self, u, l=2):
        for i in xrange(l, u + 1):
            if self.is_prime(i):
                yield i

    def smallest_factor(self, n):
        # this could be improved with an int sqrt algorithm - no need to have a float
        limit = int(math.sqrt(n))

        for p in self.primes_up_to(limit):
            if n % p == 0:
                return p
        return n

    def largest_factor(self, n):
        while not self.is_prime(n):
            n = n / self.smallest_factor(n)
        return n

    def is_probably_prime(self, n, base=2):
        return n > base and Modulo(n).power(base, n-1) == 1

p = Prime()
