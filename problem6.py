
import math

class Triangles:

    # sum of integers from 1 to n
    @staticmethod
    def triangle(n):
        return (n*n+n)/2

    # sum of cubes OR square of sum
    # 1^3 + 2^3 + 3^3 + ... + n^3
    # (1 + 2 + 3 + ... + n)^2
    # 4d square bottomed pyramid
    @staticmethod
    def sum_of_cubes(n):
        return Triangles.triangle(n) ** 2

    # sum of cubes OR square of sum
    # 1^3 + 2^3 + 3^3 + ... + n^3
    # (1 + 2 + 3 + ... + n)^2
    # 3d square bottomed pyramid
    @staticmethod
    def sum_of_squares(n):
        return n*(n+1)*(2*n+1)/6

print str(Triangles.sum_of_cubes(100) - Triangles.sum_of_squares(100))
