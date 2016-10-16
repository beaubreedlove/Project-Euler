
# Used in problem 514

gcd_cache = {}

def gcd(a, b):
    if b < a:
        tmp = a
        a = b
        b = tmp

    if gcd_cache.get(a) is None:
        gcd_cache[a] = {}
    elif gcd_cache.get(a).get(b) is not None:
        return gcd_cache.get(a).get(b)

    if a == 0:
        r = b
    else:
        r = gcd(a, b-a)

    gcd_cache[a][b] = r

    return r

def lcm(a, b):
    return a / gcd(a, b) * b
