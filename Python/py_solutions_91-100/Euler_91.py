#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and 
are joined to the origin, O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be 
formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
'''

from __future__ import print_function
from itertools import product, combinations
from math import sqrt, isclose

import timeit


try:
    xrange = range
except NameError:
    pass


def find_side_length(point, idx, sides_shared):
    # point is @ zero increment shared side
    if point[idx] == 0:
        return point[not idx], sides_shared + 1
    return sqrt(point[idx]**2 + point[not idx]**2), sides_shared

side = lambda p1, p2, idx: abs(p1[idx] - p2[idx])

def euler_91(dimension):
    count = 0
    max_x = max_y = dimension
    origin = (0, 0)
    points = product(range(dimension + 1), range(dimension + 1))
    for triangle in combinations(points, 2):
        p1, p2 = triangle
        # check if point origin is aligning the other two points to zero
        if triangle[0] == origin or p1[0] == p2[0] == 0 or p1[1] == p2[1] == 0:
            continue
        # if there are 2 or more shared sides it must be a right angle.
        sides_shared = 0
        side1, sides_shared = find_side_length(p1, 0, sides_shared)
        side2, sides_shared = find_side_length(p2, 1, sides_shared)
        if p1[0] == p2[0] or p1[1] == p2[1]:
            sides_shared += 1
            side3 = side(p1, p2, 1) if p1[0] == p2[0] else side(p1, p2, 0)
        else:
            side3 = sqrt(abs(p1[0] - p2[0])**2 + abs(p1[1] - p2[1])**2) 
        if sides_shared >= 2:
            count += 1
            continue
        a, b, c = sorted([side1, side2, side3])
        # this was giving a round-off error
        if isclose(sqrt(a**2 + b**2), c):
            count += 1
    return count

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_91(50)))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
