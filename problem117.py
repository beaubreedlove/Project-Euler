
cache = {0: 1, 1: 1, 2: 2, 3: 4, 4: 8}

def solution(n):
    ret = cache.get(n)
    if ret is not None:
        return ret

    ret = 1

    for s in range(n - 1):
        ret = ret + solution(s)

    for s in range(n - 2):
        ret = ret + solution(s)

    for s in range(n - 3):
        ret = ret + solution(s)



    cache[n] = ret

    return ret


for i in range(51):
    print "s(" + str(i) + ") = " + str(solution(i))
