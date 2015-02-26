# Sum of numbers that can be written as the sum of their fifth power. 

from __future__ import print_function

import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_30():
    fifth_pow = lambda x: x**5
    return sum([i for i in range(2, 1000000) if
                sum(map(fifth_pow, map(int, str(i)))) == i])

print("Answer: {}".format(euler_30()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
