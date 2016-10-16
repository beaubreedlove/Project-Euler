
# Maximum Digital Sum

def digital_sum(n):
    ret = 0
    while n > 0:
        ret = ret + (n % 10)
        n = n / 10
    return ret

print digital_sum(12345)

m = 0
n = 0

for i in range(0, 100):
    for j in range(0, 100):
        s = digital_sum(i ** j)
        m = max(s, m)
        n = j

print m
print n

