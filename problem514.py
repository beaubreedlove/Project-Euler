
# Geoboard Shapes

from lib.prime2 import MillerRabin, KnownPrimes
import lib.mod_arith #this was from lib.mod_arith import mod last time I tested
from lib.gcd import *
import math

#       A

#                        B


# ----------------O--------------------------

# A < 0 < B

# (B_x-A_x)*(A_y+B_y)/2+A_x*A_y/2-(B_x)*B_y/2

# (Bx - Ax)(Ay + By) + (Ax)(Ay) - (Bx)(By)
# ----------------------------------------
#                  2

# BxAy + BxBy - AxAy - AxBy + AxAy - BxBy
# ---------------------------------------
#                  2

# BxAy - AxBy
# -----------
#     2


N = 1

# calculates the area of a triangle with one point at origin
# a and b represent the other two points
# note: this function assumes the y value of a and b are positive
def area_of_triangle(a, b):
    # BxAy - AxBy
    # -----------
    #     2
    (a_x, a_y) = a
    (b_x, b_y) = b
    return float(abs(b_x * a_y - a_x * b_y)) / 2 # todo: calculate area in 1/2's so that we don't have to divide by 2. the area of every polygon will be a multiple of 1/2

class Node:
    # x,y coordinates of the node
    x = None
    y = None

    level = 0 # for debugging

    # the fathest a point can be added and still fit in an NxN board
    # top_boundary = 0 # constant
    right_boundary = None
    # bottom_boundary = N # constant
    left_boundary = None

    # the previous node in the polygon
    parent = None

    # the next nodes in the polygon
    children = []

    # all the previous nodes in the polygon
    ancestry = [] #stack

    # measured in x and y values, these mark smallest square that encloses the polygon
    # top_most_node_y = 0 # constant
    right_most_node_x = None
    bottom_most_node_y = None
    left_most_node_x = None

    # area of the current polygon if the last point was connected to the origin
    # must be populated by calling calculate_area()
    area = None

    # a count of the inner points of the current polygon - not just the current wedge
    # this includes edge points, but excludes vertexes
    # used for calculating how many times the same polygon can appear
    inner_points = None

    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

        if parent is None:
            self.level = 0
        else:
            self.level = parent.level + 1

        # initialize inner_points for root node
        if parent is None:
            self.inner_points = 0

        # initialize current polygon extremes
        if parent is None:
            self.right_most_node_x = 0
            self.bottom_most_node_y = 0
            self.left_most_node_x = 0
        else:
            self.right_most_node_x = max(parent.right_most_node_x, x)
            self.bottom_most_node_y = max(parent.bottom_most_node_y, y)
            self.left_most_node_x = min(parent.left_most_node_x, x)

        # initialize boundaries for children nodes
        self.right_boundary = self.left_most_node_x + N
        self.left_boundary = self.right_most_node_x - N

        # water the tree
        self.init_children()

    # gets area of this polygon assuming the next node is the origin
    # the return os thie method is cached in self.area because it will be called many times
    def get_area(self):
        if self.area is None:
            self.area = self.calculate_area()

        return self.area

    def calculate_area(self):
        parent_coordinates = self.get_parent_coordinates_or_zeros()
        self_coordinates = (self.x, self.y)

        area_of_current_wedge = area_of_triangle(parent_coordinates, self_coordinates)

        if self.parent is not None:
            area_of_current_wedge = area_of_current_wedge + self.parent.get_area()

        return area_of_current_wedge

    def get_parent_coordinates_or_zeros(self):
        if self.parent is None:
            return (0, 0)
        else:
            return (self.parent.x, self.parent.y)

    # counts all the inner points, including those colinear to edges, but excluding vertexes
    # this number will help calculate how many times this polygon can appear
    def get_inner_points(self):
        if self.inner_points is None:
            self.inner_points = self.calculate_inner_points()

        return self.inner_points

    # this function counts the inner points in the new wedge which weren't in the previous
    # wedge and adds all the inner points from the parent polygon
    def calculate_inner_points(self):
        new_inner_points = 0

        # if this is the origin return 0
        if self.parent is None:
            return 0

        # if this is the first non-origin point on the polygon, then we have no 3d shape yet
        # the inner points are just the ones colinear to this first edge
        if self.parent.x == 0 and self.parent.y == 0:
            # gcd is a sneaky way to do this - think about it
            return gcd(abs(self.x), self.y) # y is already positive

        # any points on y = 0 have already been dealt with in the trivial cases
        for _y in xrange(1, N + 1):
            min_x = int(math.ceil(float(_y) / self.y * self.x)) if self.y != 0 else -N
            max_x = int(math.floor(float(_y) / self.parent.y * self.parent.x)) if self.parent.y != 0 else N + 1
            for _x in xrange(min_x, max_x):
                if _y > float(self.y - self.parent.y) / (self.x - self.parent.x) * (_x - self.x) + self.y:
                    # exclude points in the wedge but outside the triangle
                    continue
                if _x == self.x and _y == self.y:
                    # exclude the new vertex
                    continue
                new_inner_points = new_inner_points + 1

        # add in parent points
        return new_inner_points + self.parent.get_inner_points()

    # returns the number of ways this polygon can fit on a NxN board unrotated
    # this number will help calculate how many times this polygon can appear
    def number_of_possible_translations(self):
        return (N - self.get_height() + 1) * (N - self.get_width() + 1)

    # returns the number of ways this polygon in this position can be created using
    # another combination (not permutation) of points (nodes)
    def number_of_congruent_untranslated_polygons(self):
        return 2 ** self.get_inner_points()

    # returns the number of polygons that can fit on an NxN grid which are congruent to this one
    def number_of_congruent_polygons(self):
        return self.number_of_congruent_untranslated_polygons() * self.number_of_possible_translations()

    # returns the total area of this polygon, and all polygons congruent to this
    def contribution_to_expected_area(self):
        return self.get_area() * self.number_of_congruent_polygons()

    # returns the total area of this polygon, all decendant polygons, and all polygons congruent to these
    def contribution_of_children_and_self_to_expected_area(self):
        area = self.contribution_to_expected_area()

        for c in self.children:
            area = area + c.contribution_to_expected_area()

        return area

    # defines children polygons and adds them to childeren list
    def init_children(self):
        # need to calculate legal range
        # if self.x > 0:
            # must be right or = to left bounrary
            # must be left of self.x
            # y must be between 0 and N inclusive
            # must satisfy _y > self.y / self.x * _x
        # elif self.x == 0:
            # must be right or = to left bounrary
            # must be left of self.x
            # y must be between 0 and N inclusive
        # else:
            # must be right or = to left boundary
            # must be left of self.x
            # y must be between 0 and N inclusive
            # must satisfy _y > - self.y / self.x * _x
        
        if self.x != 0:
            slope_of_origin_to_current_point = float(self.y) / self.x
        else:
            slope_of_origin_to_current_point = 0 # this won't be needed

        last_y = -1 # used to determine if an entire row has no valid next nodes
        for _y in xrange(0, N + 1):
            for _x in xrange(self.left_boundary, self.right_boundary):
                if self.x > 0:
                    if _y <= slope_of_origin_to_current_point * _x:
                        # the potential child point is right of the origin and
                        # the potential child point is on or below the line from the origin to the current point
                        # therefore: this point would create a concave or duplicate shape
                        break
                elif self.x < 0:
                    if _y >= slope_of_origin_to_current_point * _x:
                        # the potential child point is left of the origin and
                        # the potential child point is on or above the line from the origin to the current point
                        # therefore: this point would create a concave or duplicate shape
                        break

                if _x == self.x and _y == self.y:
                    continue

                child = Node(_x, _y, self)
                self.children.append(child)
                last_y = _y

            # if no y's on this row, then there won't be on any other rows
            if last_y != _y:
                break

    def get_width(self):
        return self.right_most_node_x - self.left_most_node_x

    def get_height(self):
        return self.bottom_most_node_y

root = Node(0, 0)

expected_area = root.contribution_of_children_and_self_to_expected_area()
denominator = N ** ((N + 1) ** 2)

print "Total expected area: " + str(expected_area)

print "Answer: " + str(float(expected_area)/denominator)




