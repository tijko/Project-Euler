## circular primes ##

import timeit
import collections
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

def euler_35():
    total = 0  
    primes = [i for i in range(2, 1000000) if is_prime(i) and 
              not any([v for v in str(i) if int(v) % 2 == 0])]
    primes.append(2)
    for prime in primes:
        circle = collections.deque([int(v) for v in str(prime)])
        for i in range(len(circle)):
            circle.rotate(1)
            num_word = ''.join([str(v) for v in circle])
            if not is_prime(int(num_word)):
                break
            if i == len(circle) - 1:
                total += 1
    return total
        
print "Answer: %s" % euler_35()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)      
