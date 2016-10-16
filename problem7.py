
# 10001st prime

from lib.prime import Prime

primes = Prime()

u = 1
l = 1

count = 0

while count < 10001:
    u = u * 2
    for p in primes.primes_up_to(u, l):
        count = count + 1
        if count == 10001:
            print p
            break
        l = p + 1
