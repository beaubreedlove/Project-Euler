
# Geoboard Shapes

from lib.prime2 import MillerRabin, KnownPrimes
from lib.gcd_cache import *
import math
from time import time

N = 10

def area_of_triangle_including_origin(a, b):
    if not isinstance(a, Point) or not isinstance(b, Point):
        raise "Something besides a Point was passed into area_of_triangle_including_origin()"
    # BxAy - AxBy
    # -----------
    #     2
    # todo: calculate area in 1/2's so that we don't have to divide by 2. the area of every polygon will be a multiple of 1/2
    return float(abs(B.x * A.y - A.x * B.y)) / 2

def point_inside_triangle_helper(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    return (p1_x - p3_x) * (p2_y - p3_y) - (p2_x - p3_x) * (p1_y - p3_y)

def point_inside_triangle(pt_x, pt_y, v1_x, v1_y, v2_x, v2_y, v3_x, v3_y):
    b1 = point_inside_triangle_helper(pt_x, pt_y, v1_x, v1_y, v2_x, v2_y) < 0
    b2 = point_inside_triangle_helper(pt_x, pt_y, v2_x, v2_y, v3_x, v3_y) < 0
    b3 = point_inside_triangle_helper(pt_x, pt_y, v3_x, v3_y, v1_x, v1_y) < 0

    return b1 == b2 and b2 == b3

def point_inside_triangle_of_origin_and_point_pair(pt_x, pt_y, pp):
    return point_inside_triangle(pt_x, pt_y, 0, 0, pp.first.x, pp.first.y, pp.second.x, pp.second.y)

class Point:

    x = None
    y = None

    def __init__(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise "Tried to instantiate Point with something that's not an integer"

        self.x = x
        self.y = y

    _unique_id = None
    def unique_id(self):
        if self._unique_id is None:
            self._unique_id = str(self.x) + "," + str(self.y)
        return self._unique_id

    _theta = None
    def theta(self):
        if self._theta is None:
            self._theta = math.atan2(self.y, self.x)
            if self._theta < 0:
                self._theta = self._theta + math.pi
        return self.theta

class PointPair:

    first = None
    second = None

    # the 2nd will look like this:
    # {
    #   -N      : [(-N, 0), (-N, 1), ... (-N, N)],
    #   -N + 1  : [(-N + 1, 0), (-N + 1, 1), ... (-N + 1, N)]
    #   ...
    #   0       : [(0, 1), ... (0, N)]
    # }
    children_by_x_position_of_second = None

    def __init__(self, first, second):
        if not isinstance(first, Point) or not isinstance(second, Point):
            raise "Tried to instantiate PointPair with something that's not a Point"

        self.first = first
        self.second = second

    _area = None
    def area(self):
        if self._area is None:
            self._area = area_of_triangle_including_origin(self.first, self.second)
        return self._area

    _unique_id = None
    def unique_id(self):
        if self._unique_id is None:
            self._unique_id = self.first.unique_id() + "|" + self.second.unique_id()
        return self._unique_id

    _theta = None
    def theta(self):
        if self._theta is None:
            self._theta = math.atan2(self.second.y - self.first.y, self.second.x - self.first.x)
        return self.theta

    # keys for all max_x_value
    _area_contributed_by_self_and_children = {}

    def area_contributed_by_self_and_children(self, max_x_value):
        if !self._area_contributed_by_self_and_children.get(max_x_value):
            self._area_contributed_by_self_and_children[max_x_value] = self.calculate_area_contributed_by_self_and_children(max_x_value)
        return self._area_contributed_by_self_and_children.get(max_x_value)

    def calculate_area_contributed_by_self_and_children(self, max_x_value):
        # AREA CONTRIBUTED TO SELF needs to know about inherited inners
        # AREA CONTRIBUTED TO CHILDREN needs to know about max_x_value and inherited inners
        if max_x_value < N:
            return self.area_contributed_by_self_and_children(max_x_value + 1) + self.area_contributed_by_children_from_column(max_x_value - N)
        
        # start with self
        total_area = self.area_contributed_by_self()

        for x in xrange(0, N + 1):
            total_area = total_area + area_contributed_by_children_from_column(x)

        return total_area

    def area_contributed_by_children_from_column(self, x):
        # Don't need to cache this
        children = self.children_by_x_position_of_second.get(x)

        if children is None or len(children) == 0:
            return 0

        total_area = 0

        for x in children:
            total_area = total_area + children[x].area_contributed_by_self_and_children()

        return total_area

    _area_contributed_by_self = None
    def area_contributed_by_self(self):
        if self._area_contributed_by_self is None:
            self._area_contributed_by_self = self.area() * self.possible_translations() * self.possible_repeats()
        return self._area_contributed_by_self

    def possible_trnaslations(self):
        return (2 * N + 1 - self.width()) * (N + 1 - self.height())

    def possible_repeats(self):
        return inherited_inners + self.inners()


    def inners(self):
        # todo: This could be improved
        min_x = min(0, self.first.x, self.second.x)
        min_y = min(0, self.first.y, self.second.y)
        max_x = max(0, self.first.x, self.second.x)
        max_x = max(0, self.first.x, self.second.x)

        result = 0

        for x in xrange(min_x, max_x + 1):
            for y in xrange(min_y, max_y + 1):
                if point_inside_triangle_of_origin_and_point_pair(x, y, self):
                    result = result + 1

        return result

    def attach_child(self, pp):
        # LEFT OFF HERE
        # TODO: HOW DO WE DEAL WITH VARIABLE NUMBER OF INHERITED INNERS?
        # One solution: Pass inherited_inners into area_contributed_by_self_and_children() down to inners()
        self.children_by_x_position_of_second[pp.second.x].append(pp)


class PointCollection:

    items = {}

    def push(self, p):
        if not isinstance(p, Point):
            raise "Tried to PointCollection.push() something that's not a Point"
        unique_id = p.unique_id()

        self.items[unique_id] = p

class PointPairCollection:

    items = []

    items_indexed_by_start = {}

    def push(self, pp):
        if not isinstance(pp, PointPair):
            raise "Tried to PointPairCollection.push() something that's not a PointPair"

        # items
        self.items.append(pp)



## start script

start_time = time()

point_collection = PointCollection()
point_pair_collection = PointPairCollection()

for i in xrange(-N, N + 1):
    min = 0 if i != 0 else 1
    for j in xrange(min, N + 1):
        p = Point(i, j)
        point_collection.push(p)

for p1 in point_collection.items:
    for p2 in point_collection.items:
        if p2.theta() > p1.theta():
            pair = PointPair(p1, p2)
            point_pair_collection.push(pair)

raise "TODO: Precalculate all PointPair children. No nodes on positive x-axis have parents; negative x-access have children. INDEX THEM IN THEIR PROPER children_by_x_position_of_second!!!"
raise "inherited_inners for a root should be the points on the trailing edge"

# for all point pairs that start with self.second
#     if convex valid
#         attach child

print "took " + str(time() - start_time) + " seconds"

print "Points: " + str(len(point_collection.items))
print "PointPairs: " + str(len(point_pair_collection.items))



