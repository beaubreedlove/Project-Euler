
import math
from modulo import Modulo

# Used in problem 3

class Prime:
    # def is_prime(self, n):
    # def primes_up_to(self, n):  #generator
    # def smallest_factor(self, n):
    # def largest_factor(self, n):
    # def nth(self, n):




    def is_probably_prime(self, n, base=2):
        return n > base and Modulo(n).power(base, n-1) == 1

p = Prime()
