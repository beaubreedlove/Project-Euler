
# Multiples of 3 and 5

# Sums all multiples of `factors` less than `limit`
def sum_multiples(factors, limit):
    sum = 0
    for i in xrange(1,limit):
        for x in factors:
            if i % x == 0:
                sum = sum + i
                break
    return sum

print sum_multiples([3,5], 1000)
