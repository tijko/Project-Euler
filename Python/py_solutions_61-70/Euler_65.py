#!/usr/bin/env python
# -*- coding: utf-8 -*-

# for the constant e find the sum of the 10000 convergents numerator

from __future__ import print_function

import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_65():
    n = 2
    periods = [2,1]
    for i in range(33):
        periods += [n, 1, 1]
        n += 2
    old_n = 8
    old_d = 3
    n = 11
    d = 4
    convergents = list()
    for c in xrange(4, len(periods)):
        new_n = (n * periods[c]) + old_n
        new_d = (d * periods[c]) + old_d
        old_n = n
        old_d = d
        n = new_n
        d = new_d
        convergents.append([new_n, new_d])
    total = sum([int(i) for i in str(convergents[95][0])])
    return total

if __name__ == '__main__':
    print("Answer: %s" % euler_65())
    stop = timeit.default_timer()
    print("Time: %f" % (stop - start))
