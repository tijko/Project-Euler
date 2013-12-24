# what is the largest prime factor of 600851475143 ? 

import math
import timeit


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
    high = 0
    for i in xrange(1, 1000000, 2):
        if is_prime(i) and 600851475143 % i == 0 and i > high:
            high = i
    return high


print "Answer: %s" % euler_3()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
