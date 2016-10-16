"""
g(k) = 1 for 0 <= k <= 1999
g(k) = g(k-2000) + g(k-1999) for k >= 2000

find g(10^18) mod 20092010
"""

cache = {}

# warm cache
for k in range(2000):
    cache[k] = 1

def g(k):
    r = cache.get(k)
    if r is not None:
        return r

    r = (g(k-2000) + g(k-1999)) % 20092010

    cache[k] = r

    return r

hundred_more = 100

for k in xrange(10**18):
    s = g(k)
    if k % 1000000 == 0 or hundred_more < 100:
        print "g(" + str(k) + ") = " + str(s)
    if s == 1 and k > 2000:
        print "g(" + str(k) + ") = " + str(s)
        hundred_more = 99
    if hundred_more != 100:
        hundred_more = hundred_more - 1
    if hundred_more == 0:
        break

