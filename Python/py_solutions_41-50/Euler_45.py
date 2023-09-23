#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

from __future__ import print_function
import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_45():
    triangle = {i * (i + 1) / 2 for i in range(286, 100000)}
    pent = [(i * (3 * i - 1) / 2) for i in range(166, 100000)]
    hexa = [(i * (2 * i - 1)) for i in range(144, 100000)]
    return list(triangle.intersection(pent, hexa))[0]

print("Answer: %s" % euler_45())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
