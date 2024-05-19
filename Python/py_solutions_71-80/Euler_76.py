#!/usr/bin/env python
# -*- coding: utf-8 -*-

# How many different ways can 100 hundred be written by adding at least two
# numbers

from __future__ import print_function

import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_76():
    ways = [0] * (100 + 1)
    ways[0] = 1
    for i in range(1, 100):
        for j in range(i, 101):
            ways[j] += ways[j - i]
    return ways[100]

print("Answer: %s" % euler_76())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))


