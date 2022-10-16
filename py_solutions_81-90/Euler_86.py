#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a 
fly, F, sits in the opposite corner. By travelling on the surfaces of the room 
the shortest "straight line" distance from S to F is 10 and the path is shown
on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid 
and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring 
rotations, with integer dimensions, up to a maximum size of M by M by M, for 
which the shortest route has integer length when M = 100. This is the least 
value of M for which the number of solutions first exceeds two thousand; the 
number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one 
million.
'''

from __future__ import print_function
from collections import defaultdict
from math import fmod

import timeit

try:
    range = xrange
except NameError:
    pass


def sq(limit):
    return {i:i**2 for i in range(2, limit + 1)}

def find_sq_pair(n):
    xy_sq = sq(n * 2)
    z_sq = sq(n)
    sq_dict = defaultdict(list)
    for xy in xy_sq:
        for z in z_sq:
            if z < xy / 2: continue
            if fmod(sum([xy_sq[xy], z_sq[z]])**0.5, 1) == 0:
                sq_dict[xy].append(z)
    return sq_dict

def euler_86():
    limit = 1
    total = 0
    sq_dict = find_sq_pair(2000)
    while total < 10**6:
        total = 0
        limit += 1
        for xy in sq_dict:
            if xy > limit * 2: continue
            for z in sq_dict[xy]:
                if not z <= limit: continue
                if z > xy:
                    occ = int(xy / 2)
                else:
                    if xy % 2 == 0:
                        occ = (z - int(xy / 2)) + 1
                    else:
                        occ = (z - int(xy / 2)) 
                total += occ
    return limit

if __name__ == "__main__":
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_86()))
    stop = timeit.default_timer()
    print('Time: {0:9.5}'.format(stop - start))
