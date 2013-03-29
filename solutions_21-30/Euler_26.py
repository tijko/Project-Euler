### Largest sequence of repeating numbers of n < 1000 of 1/d

import timeit
import math


start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in xrange(3, int(math.sqrt(x) + 1), 2):
        if x % i == 0:
            return False
    return True


def euler_26():
    primes_to_onethousand = [i for i in xrange(1, 1000) if is_prime(i)]
    return primes_to_onethousand[len(primes_to_onethousand) - 3]


print "Answer: %s" % euler_26()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
