#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution.
'''

from __future__ import print_function

from math import ceil
import timeit

try:
    range = xrange
except NameError:
    pass


def euler_85():
    n = 3
    close = 0
    close_area = 0
    limit = 2100000
    target = 2000000
    while True:
        mul = n if n % 2 != 0 else n + 1
        inc = ceil(float(n) / 2) # float cast for py2
        acc = 0
        for i in range(1, n + 1):
            acc += inc * i
            rects = mul * acc
            if abs(target - rects) < abs(target - close):
                close_area = n * i
                close = rects
            if rects > limit:
                break
        if i == 2:
            return close_area
        n += 1
                
if __name__ == "__main__":
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_85()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
