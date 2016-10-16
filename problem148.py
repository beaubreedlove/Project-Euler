
# Exploring Pascal's TRiangle

cache = {}

def pascal(i, j):
    c = (i, j)

    ret = cache.get(c)
    if ret is not None:
        return ret

    if i == 0 and j == 0:
        ret = 1
    elif j < 0 or j > i:
        ret = 0
    else:
        ret = (pascal(i - 1, j) + pascal(i - 1, j - 1)) % 7

    cache[c] = ret

    return ret


def count7(n):
    c = 0
    for i in xrange(n):
        for j in xrange(i + 1):
            if pascal(i, j) != 0:
                c = c + 1
    return c

for i in xrange(101):
    print "f(" + str(i) + ") = " + str(count7(i))





