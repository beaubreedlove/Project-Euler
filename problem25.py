
# problem 25: 1000 digit fibonacci

import math

cache = {0: 0, 1: 1}

def fib(n):
    ret = cache.get(n)

    if ret is not None:
        return ret

    ret = fib(n-1) + fib(n-2)

    cache[n] = ret

    return ret


i = 2
f = fib(i)

while math.log(f, 10) < 999:
    i = i + 1
    f = fib(i)

print i
print f
