
# Maximum path sum I

import math

f = open('problem18/triangle.txt')

sum_triangle = {}

i = 0
for line in list(f):
    sum_triangle[i] = {}

    j = 0
    for n in line.strip().split(' '):
        n = int(n)

        if i == 0:
            sum_triangle[i][j] = n
        elif j == 0:
            sum_triangle[i][j] = sum_triangle[i-1][j] + n
        elif j == i:
            sum_triangle[i][j] = sum_triangle[i-1][j-1] + n
        else:
            sum_triangle[i][j] = max(sum_triangle[i-1][j], sum_triangle[i-1][j-1]) + n

        j = j + 1

    i = i + 1

largest = 0

last_row = sum_triangle[len(sum_triangle)-1]

for n in last_row:
    if last_row[n] > largest:
        largest = last_row[n]

print largest

