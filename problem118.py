
from lib.prime2 import MillerRabin, KnownPrimes
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

def permutations_using_array(input):
    if len(input) == 0:
        return []
    if len(input) == 1:
        return [input]

    result = []

    for i in range(len(input)):
        first = input[i]
        rest = copy(input)
        rest.pop(i)

        for sub_result in permutations_using_array(rest):
            result.append([first] + sub_result)

    return result

def copy(a):
    b = []
    for e in a:
        b.append(e)
    return b


for e in permutations_using_array([9,8,7,6,5,4,3,2,1]):
    n = e[0] + 10 * (e[1] + 10 * (e[2] + 10 * (e[3] + 10 * (e[4] + 10 * (e[5] + 10 * (e[6] + 10 * (e[7] + 10 * e[8])))))))
    if is_prime(n):
        print n
