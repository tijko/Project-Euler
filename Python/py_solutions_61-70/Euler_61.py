#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 cyclic number of six 4-digit that are in one of each and doesn't have to be
 in ranking order (i.e. tri,sq,pent...)

 triangle = n * (n + 1) / 2
 square   = n**2
 pentagon = n * (3*n - 1) / 2
 hexagon  = n * (2*n - 1)
 heptagon = n * (5*n - 3) / 2
 octagon  = n * (3*n - 2)
'''

from __future__ import print_function
from sys import setrecursionlimit

from functools import partial
import itertools
import timeit


try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def create_four_digit_polygonal_set(lower_bound, upper_bound, polygon_fn):
    polygonal_set = list()
    n = 1
    while polygon_fn(n) < upper_bound:
        polygonal_number = polygon_fn(n)
        if polygonal_number > lower_bound:
            polygonal_set.append(polygonal_number)
        n += 1
    return polygonal_set

def match_cyclical_pair(p1, p2):
    ps1, ps2 = map(str, [p1, p2])
    if ps1[:2] == ps2[2:] or ps1[2:] == ps2[:2]:
        return True
    return False

def find_cyclic_set(n, c_set, cyclic, cyclic_idx):
    if len(c_set) == 6:
        return c_set
    # XXX check the wrap on the last polygonal-number
    for polygonal_number in cyclic[cyclic_idx]:
        if match_cyclical_pair(n, polygonal_number):
            return find_cyclic_set(polygonal_number, c_set + [n], cyclic, cyclic_idx + 1)
    n = c_set.pop(-1)
    return find_cyclic_set(n, c_set, cyclic, cyclic_idx - 1)

def euler_61():
    triangle = lambda n: int(n * (n + 1) / 2)
    square   = lambda n: n * n
    pentagon = lambda n: int(n * (3 * n - 1) / 2)
    hexagon  = lambda n: n * (2 * n - 1)
    heptagon = lambda n: int(n * (5 * n - 3) / 2)
    octagon  = lambda n: n * (3 * n - 2)
    polygonal_four_digit = partial(create_four_digit_polygonal_set, 999, 10000)
    cyclic = list(map(polygonal_four_digit, [triangle, square, pentagon,
                                             hexagon, heptagon, octagon]))
    return sum(find_cyclic_set(cyclic[0][0], [], cyclic, 0))

if __name__ == '__main__':
    recursion_limit = 3000
    setrecursionlimit(recursion_limit)
    print("Answer: {}".format(euler_61()))
    stop = timeit.default_timer()
    print("Time: {:.4f}".format(stop - start))