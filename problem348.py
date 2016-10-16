
"""
Many numbers can be expressed as the sum of a square and a cube. Some of them in more than one way.

Consider the palindromic numbers that can be expressed as the sum of a square and a cube, both greater than 1, in exactly 4 different ways.
For example, 5229225 is a palindromic number and it can be expressed in exactly 4 different ways:

2285^2 + 20^3
2223^2 + 66^3
1810^2 + 125^3
1197^2 + 156^3

Find the sum of the five smallest such palindromic numbers.
"""

def is_palindrome(n):
    n = str(n)
    for i in xrange((len(n)+1)/2):
        if n[i] != n[-1-i]:
            return False
    return True

a_big_number = 1e9

square_base = 1
square = 1
cube_base = 1
cube = 1

squares = set()
cubes = set()

while square <= a_big_number:
    square_base = square_base + 1
    square = square_base ** 2
    squares.add(square)

while cube <= a_big_number:
    cube_base = cube_base + 1
    cube = cube_base ** 3
    cubes.add(cube)

# print squares

# print cubes

sums = {}

for s in squares:
    for c in cubes:
        n = s + c
        if is_palindrome(n):
            sums[n] = sums.get(n, 0) + 1

result = 0

for s in sums:
    if sums[s] == 4:
        result = result + s

print result
