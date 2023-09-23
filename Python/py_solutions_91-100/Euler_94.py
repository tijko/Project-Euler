#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
It is easily proved that no equilateral triangle exists with integral length 
sides and integral area. However, the almost equilateral triangle 5-5-6 has an 
area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two 
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral 
side lengths and area and whose perimeters do not exceed one billion 
(1,000,000,000).
'''

from __future__ import print_function

import timeit


limit = 10**9

def integral_equilaterals(a, b, c, total, step, switch):
    perimeter = sum([a, b, c])
    if perimeter > limit: return total
    else: total += perimeter
    if switch:
        b2, c2 = b, c
        c = step + a + b + c + 5
        a = b = c - 1
    else:
        b2, c2 = b, c
        c = step + a + b + c
        a = b = c + 1
    # recurse, increasing the step by b, c
    # even if b is +1 on c or c +1 on b you increase the step by
    # the +1 side and the other.  then flip the switch to show
    # which side will be +1
    return integral_equilaterals(a, b, c, total, step + b2 + c2, not switch)

def euler_94():
    a, b, c = 5, 5, 6
    step = b + c
    perimeter_sum = sum([a, b, c])
    # set the next a,b,c set. incrementing a, b to start
    # then alternating as the sets progress ((a, b) + 1 then (c) + 1)
    a, b, c = perimeter_sum + 1, perimeter_sum + 1, perimeter_sum
    perimeter_sum += integral_equilaterals(a, b, c, 0, step, True)
    return perimeter_sum
 
if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_94()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
