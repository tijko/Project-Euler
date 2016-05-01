#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and 
six red discs, and two discs were taken at random, it can be seen that the 
probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two 
blue discs at random, is a box containing eighty-five blue discs and thirty-five 
red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs 
in total, determine the number of blue discs that the box would contain.
'''

from __future__ import print_function

import timeit


limit = 10**12

def arranged_probability(b1, b2, combined_discs):
    discs = int(combined_discs**0.5)
    if discs > limit: return b1
    b2 = b1 * 2 + b2 + discs * 2
    return arranged_probability(b2 + 1, b2, (b2 + 1) * b2 * 2)

def euler_100():
    b1, b2 = 3, 2
    return arranged_probability(b1, b2, b1 * b2 * 2)

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_100()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
