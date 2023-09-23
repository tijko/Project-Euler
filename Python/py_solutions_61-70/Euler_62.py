#!/usr/bin/env python
# -*- coding: utf-8 -*-

# find the smallest cube that can be permutated to 5 other cubes 

from __future__ import print_function

import itertools
import timeit


try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_62():
    cubes = [sorted([v for v in str(i**3)]) for i in range(10001)]
    for cube in cubes:
        if cubes.count(cube) == 5:
            return (cubes.index(cube)**3)

print("Answer: %s" % euler_62())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
