
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 cyclic number of six 4-digit that are in one of each and doesn't have to be
 in ranking order (i.e. tri, sq, pent...)

 the sequence is considered two-digits leading into the next number
 (e.g. 1245 -> 4590)

 then the 'wrap' sequence is the last two-digits 'wrapping' around to the
 leading number (e.g. 1245 -> 4590 -> 9012)

 triangle = n * (n + 1) / 2
 square   = n**2
 pentagon = n * (3*n - 1) / 2
 hexagon  = n * (2*n - 1)
 heptagon = n * (5*n - 3) / 2
 octagon  = n * (3*n - 2)
'''

from __future__ import print_function

from collections import defaultdict
from functools import partial
from sys import setrecursionlimit

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

def match_lists(poly, poly_hash, c_set):
    if not poly_hash[poly]:
        return c_set
    for p in poly_hash[poly]:
        return match_lists(p, poly_hash, c_set + [p])

def euler_61():
    triangle = lambda n: int(n * (n + 1) / 2)
    square   = lambda n: n * n
    pentagon = lambda n: int(n * (3 * n - 1) / 2)
    hexagon  = lambda n: n * (2 * n - 1)
    heptagon = lambda n: int(n * (5 * n - 3) / 2)
    octagon  = lambda n: n * (3 * n - 2)
    polygonal_four_digit = partial(create_four_digit_polygonal_set, 999, 10000)
    cyclical_sets = list(map(polygonal_four_digit, [triangle, square, pentagon,
                                                    hexagon, heptagon, octagon]))
    polygonal_matches = defaultdict(dict)
    for idx, cyclical_set in enumerate(cyclical_sets):
        for polygonal_number in cyclical_set:
            polygonal_matches[polygonal_number] = dict()
            for match_idx, match_set in enumerate(cyclical_sets):
                if match_idx == idx: continue
                for sequence in match_set:
                    if match_cyclical_pair(polygonal_number, sequence):
                        polygonal_matches[polygonal_number].update(polygonal_matches
    for match in polygonal_matches:
        print('Polygonal: {} Type: {}'.format(match[1], match[0] + 3))
        print('{}'.format(['{} - {}'.format(i[1], i[0] + 3) for i in polygonal_matches[match]]))

if __name__ == '__main__':
    setrecursionlimit(2000000)
    print("Answer: {}".format(euler_61()))
    stop = timeit.default_timer()
    print("Time: {:.4f}".format(stop - start))
