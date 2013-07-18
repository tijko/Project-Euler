## smallest prime for which replacing part of the number you can form 8 different primes ##
## Example: 189-00-37, 189-33-37, 189-44-37, 189-55-37, 189-66-37, 189-77-37, 189-88-37, 189-99-37 ##
## the replacement digits do not have to be adjacent or consecutive but, have to be the same ##

import timeit
import math


start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def euler_51():
    primes = list() 
    for i in xrange(10000, 1000000):
        if is_prime(i):
            for v in str(i):
                if str(i).count(v) > 2:
                    primes.append(str(i))
    for prime in primes:
        for i in prime:
            if prime.count(i) > 2:
                count = 0
                for v in xrange(1, 10):            
                    if is_prime(int(prime.replace(i, str(v)))):
                        count += 1
                if count > 7:
                    return prime

print "Answer: %s" % euler_51()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
