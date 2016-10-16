
# Consecutive prime sum

from lib.prime2 import MillerRabin, KnownPrimes

x = 1000000

def is_prime(n):
    if KnownPrimes.is_prime(n):
        return True

    if KnownPrimes.is_composite(n):
        return False

    if MillerRabin.is_prime(n):
        KnownPrimes.save_prime(n)
        return True

    return False

consecutive_primes = []

for n in xrange(2, x):
    if MillerRabin.is_prime(n):
        consecutive_primes.append(n)

KnownPrimes.save_consecutive_primes(consecutive_primes, 1e6)

max_length = 0
max_sum = 0
max_list = []

i = 0
while i < len(consecutive_primes):
    j = i
    sum_of_primes = 0
    number_of_primes = 0
    curr_list = []
    while sum_of_primes < x and i + j < len(consecutive_primes):
        sum_of_primes = sum_of_primes + consecutive_primes[j]
        number_of_primes = number_of_primes + 1
        curr_list.append(consecutive_primes[j])

        if number_of_primes > max_length and is_prime(sum_of_primes) and sum_of_primes < x:
            print "current longest is " + str(number_of_primes) + " primes summing " + str(sum_of_primes) + ": " + str(curr_list)
            max_length = number_of_primes
            max_sum = sum_of_primes
            max_list = curr_list

        j = j + 1
    i = i + 1

print "Result: " + str(max_sum)

for p in max_list:
    if MillerRabin.is_prime(p):
        pass
    else:
        print str(p) + " IS NOT PRIME!!!"



