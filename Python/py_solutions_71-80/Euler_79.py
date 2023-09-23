#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown
# length.

from __future__ import print_function

import timeit
import os

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_79():
    pin = ''
    with open('/home/tijko/Project-Euler/euler_txt/keylog.txt') as f:
        key_series = f.read()
    key_series = key_series.split()
    key_series = [[v for v in i] for i in key_series]
    digits = set([i for v in key_series for i in v])
    pin_length = len(digits)
    while len(pin) < pin_length:
        for digit in digits:
            single = [v.index(digit) for v in key_series if digit in v]
            if all(j==0 for j in single):
                pin += digit
                key_series = [[j for j in v if j != digit] for v in key_series]
                digits.remove(digit)
                break
    return pin

print("Answer: %s" % euler_79())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
