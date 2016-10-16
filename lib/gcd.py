
# Used in problem 5

def gcd(a, b):
    if b < a:
        tmp = a
        a = b
        b = tmp
    if a == 0:
        return b
    return gcd(a, b-a)

def lcm(a, b):
    return a / gcd(a, b) * b
