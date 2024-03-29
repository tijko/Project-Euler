#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find the smallest integer n -- where n2, n3, n4, n5, n6 all contain the same digits but, in different order 

from __future__ import print_function

import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_52():
    permute_mul = 100
    while True:
        if all(set(str(permute_mul * i)) == set(str(permute_mul * 2)) for i in range(3, 7)):
            return permute_mul
        permute_mul += 1
                        
print("Answer: %d" % euler_52())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
