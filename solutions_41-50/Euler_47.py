# find the first of the four consecutive integer to have four distinct prime factors. 

import timeit
import math


start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in xrange(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True
    

def euler_47():
    composites = [i for i in xrange(10000, 265000) if not is_prime(i)]
    primes = [i for i in xrange(2, 1000) if is_prime(i)]
    four_factors = list()
    for composite in composites:
        if len([prime for prime in primes if composite % prime == 0]) >= 4:
            four_factors.append(composite)
    for i in xrange(len(four_factors)):
        if four_factors[i:i+4] == range(four_factors[i], four_factors[i]+4):
            return four_factors[i]

print "Answer: %s" % euler_47()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
