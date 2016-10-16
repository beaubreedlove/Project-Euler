
# Smallest multiple

from lib.gcd import *

m = 1

for i in xrange(1, 11 + 1):
    m = lcm(m, i)

print m

