#!/usr/bin/env python
## largest concatenated pandigital number from product

from __future__ import print_function

import timeit
from string import digits

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_38():
    pandigitize = lambda x, y: x * y
    return max([''.join([i for i in str(map(pandigitize, [i] * 2, [1, 2])) if i.isdigit()]) for i in range(192, 10000) if ''.join(sorted([k for k in str(map(pandigitize, [i] * 2, [1, 2])) if k.isdigit()])) == digits[1::]])

print("Answer: %s" % euler_38())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))

