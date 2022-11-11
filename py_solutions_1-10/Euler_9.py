#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find the only pythagorean triplet that a + b + c = 1000 

from __future__ import print_function

import math
import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()


def euler_9():
    for x in range(1, 1000):
        for y in range(x+1, 1000):
            z = (x**2 + y**2)**0.5
            if x + y + z == 1000:
                return x * y * z

print('Answer: {}'.format(euler_9()))
stop = timeit.default_timer()
print('Time: {0:9.5f}'.format(stop - start))
