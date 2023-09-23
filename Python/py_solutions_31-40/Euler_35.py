## circular primes ##

import timeit
import math

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def euler_35():
    return sum([1 for prime in (j for j in map(str, range(2, 1000000)) if is_prime(int(j)) and (int(j) == 2 or not any(int(v) % 2 == 0 for v in j))) if all(is_prime(int(''.join(prime[i:] + prime[:i]))) for i in range(1, len(prime)))]) 

                   
print("Answer: %s" % euler_35())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
  
