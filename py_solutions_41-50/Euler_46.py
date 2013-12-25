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

def euler_46():   
    composite = 10
    while True:
        while composite % 2 == 0 and is_prime(composite):
            composite += 1
        total = [2 * v**2 for v in xrange(int(math.sqrt(composite)) // 2)]
        primes = (k for k in xrange(composite + 1) if is_prime(k))
        for v in total:
            for j in primes:
                odds = total[v] + j 
                if odds == composite: 
                    break 
            if odds == composite: 
                break 
        if odds != composite:
            return composite

print "Answer: %s" % euler_46()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
