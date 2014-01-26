# Truncatable primes from left to right ---> 
# Ex: 3797 ~ 797 ~ 97 ~ 7 and 3797 ~ 379 ~ 37 ~ 3 

import math
import timeit


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

def euler_37():
    return sum([p for p in (i for i in xrange(11, 1000000) if is_prime(i) and not set(str(i)).intersection(['0', '4', '6', '8'])) if all(is_prime(int(str(p)[:-v])) for v in xrange(1, len(str(p)))) and all(is_prime(int(str(p)[v:])) for v in xrange(1, len(str(p))))])

print "Answer: %s" % euler_37()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
