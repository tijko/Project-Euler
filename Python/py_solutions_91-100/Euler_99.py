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
    # mark first pair as highest to start
    high_base, high_exp, high_idx = *pairs[0], 1
    for idx, pair in enumerate(pairs[1:], 2):
        curr_base, curr_exp = pair
        # creates a workable exponent by determining which of 
        # exponents being compared is larger, then taking
        # that ratio of (large_exp / small_exp) * 2 and the base
        # of the small_exp gets raised to the second power.
        if high_exp > curr_exp:
            exp1, exp2 = 2 * (high_exp / curr_exp), 2
        else:
            exp1, exp2 = 2, (curr_exp / high_exp) * 2
        if high_base**exp1 < curr_base**exp2:
            high_base, high_exp, high_idx = *pair, idx
    return high_idx
    
if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_99(pairs)))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
