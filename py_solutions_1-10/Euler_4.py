# Find the largest palindrome number made from the product of two 3-digit numbers?

from __future__ import print_function

import itertools
import operator 
import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_4():
    canidates = itertools.combinations(range(100, 1000), 2)
    palindrome_check = lambda x: (str(operator.mul(*x)) ==  
                                  str(operator.mul(*x))[::-1])
    return max([operator.mul(*i) for i in canidates if palindrome_check(i)])

print("Answer: {}".format(euler_4()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
