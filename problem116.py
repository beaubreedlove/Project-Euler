

red_cache = {0: 0, 1: 0}

def red(n):
    ret = red_cache.get(n)
    if ret is not None:
        return ret

    ret = 0

    for s in range(n - 1):
        ret = ret + red(s) + 1

    red_cache[n] = ret

    return ret


green_cache = {0: 0, 1: 0, 2: 0}

def green(n):
    ret = green_cache.get(n)
    if ret is not None:
        return ret

    ret = 0

    for s in range(n - 2):
        ret = ret + green(s) + 1

    green_cache[n] = ret

    return ret

blue_cache = {0: 0, 1: 0, 2: 0, 3: 0}

def blue(n):
    ret = blue_cache.get(n)
    if ret is not None:
        return ret

    ret = 0

    for s in range(n - 3):
        ret = ret + blue(s) + 1

    blue_cache[n] = ret

    return ret



for i in xrange(51):
    print "red(" + str(i) + ") = " + str(red(i))


for i in xrange(51):
    print "green(" + str(i) + ") = " + str(green(i))


for i in xrange(51):
    print "blue(" + str(i) + ") = " + str(blue(i))

print "----------------------"

print str(red(50) + green(50) + blue(50))


