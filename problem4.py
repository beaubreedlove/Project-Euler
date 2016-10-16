
# Largest palindrome product

def is_palindrome(a):
    a = str(a)
    eos = len(a)-1
    for i in xrange(0, eos/2+1):
        if a[i] != a[eos-i]:
            return False
    return True

factor_length = 3

min_factor = pow(10, factor_length-1)
max_factor = pow(10, factor_length) - 1

largest_product = 0

for sum in xrange(2 * max_factor, 2 * min_factor - 1, -1):
    for a in xrange(sum / 2, min_factor - 1, -1):
        b = sum - a
        if b > max_factor:
            break
        product = a * b
        if product > largest_product:
            if is_palindrome(product):
                largest_product = product
                break
        else:
            break

if largest_product != 0:
    print largest_product
else:
    print "There is no palindrome product."
