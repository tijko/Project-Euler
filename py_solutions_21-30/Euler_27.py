# Find the product of the coefficients, a and b, for the quadratic 
# expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import math
import timeit
import itertools


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


def euler_27():
    max_primes = 0
    quadratic = lambda x, y, z: x**2 + (x * y) + z
    for i, v in itertools.product(xrange(-999, 1000), xrange(-999, 1000)):
        primes = 0
        q = quadratic(primes, v, i) 
        while is_prime(abs(q)):
            primes += 1
            q = quadratic(primes, v, i)
        if primes > max_primes:
            max_primes = primes
            co_prod =  i * v
    return co_prod


print "Answer: %s" % euler_27()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
