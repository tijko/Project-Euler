# composite odd numbers that aren't the sum of a prime twice a square 

import timeit
import math


start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in xrange(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

def composite_gen():
    composite = 2
    while True:
        while composite % 2 == 0 or is_prime(composite):
            composite += 1
        yield composite
        composite += 1

def composite_chk(comp, twice_exp, primes):
    for exp in twice_exp:
        for prime in primes:
            if exp + prime == comp:
                return False
    return True

def euler_46():   
    cg = composite_gen() 
    while True:
        composite = cg.next() 
        twice_exp = (2 * v**2 for v in xrange(int(math.sqrt(composite))))
        primes = [k for k in xrange(composite + 1) if is_prime(k)]
        if composite_chk(composite, twice_exp, primes): return composite        


print "Answer: %s" % euler_46()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
