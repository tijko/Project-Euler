# what is the largest prime factor of 600851475143 ? 

from __future__ import print_function

import math
import timeit


try:
    range = xrange
except NameError:
    pass
 
start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def euler_3():
    FACTOR_OF = 600851475143
    return max([i for i in range(1, int(math.sqrt(FACTOR_OF)) + 1, 2) 
                if FACTOR_OF % i == 0 and is_prime(i)])


print("Answer: {}".format(euler_3()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
