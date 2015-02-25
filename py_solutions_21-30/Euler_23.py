# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. 

from __future__ import print_function

import timeit

try:
    from itertools import ifilterfalse as filterfalse
except ImportError:
    from itertools import filterfalse

from itertools import combinations_with_replacement

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()


def euler_23():
    abundant = (i for i in range(28124) if i < 
                sum(filterfalse(lambda x, i=i: i % x, range(1, i // 2 + 1))))
    abundant_sums = {i for i in combo_gen(abundant)}
    return sum(abundant_sums.symmetric_difference(range(28124)))

def combo_gen(x):
     for i in combinations_with_replacement(x, 2):
         if sum(i) < 28124:
            yield sum(i)


print("Answer: {}".format(euler_23()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
