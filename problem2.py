
# Even fibonacci numbers

sum = 0

prev = 1
fib = 0

while fib <= 4000000:
    tmp = fib
    fib = fib + prev
    prev = tmp

    if fib % 2 == 0:
        sum = sum + fib

print str(sum)
