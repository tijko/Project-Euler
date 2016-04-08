#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more 
difficult, as both numbers contain over three million digits.

Using base_exp.txt, a 22K text file containing one thousand lines with a 
base/exponent pair on each line, determine which line number has the greatest 
numerical value.

NOTE: The first two lines in the file represent the numbers in the example given
above.
'''

from __future__ import print_function, division

import timeit
import os


path = os.getcwd().strip('py_solutions_91-100')

with open(path + 'euler_txt/base_exp.txt') as f:
    pairs = [list(map(int, pair.split(','))) for pair in f.readlines()]

def euler_99(pairs):
    high, high_idx = pairs[0], 1
    for idx, pair in enumerate(pairs[1:], 2):
        b1, b2 = high[0], pair[0]
        if high[1] > pair[1]:
            x1, x2 = 2 * (high[1] / pair[1]), 2
        else:
            x1, x2 = 2, (pair[1] / high[1]) * 2
        if b1**x1 < b2**x2:
            high = pair
            high_idx = idx
    return high_idx
    
if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_99(pairs)))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
