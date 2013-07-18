# What is the 10001st prime number?

import math
import timeit


start = timeit.default_timer()

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

def prime_gen():
    number_prime = 0
    n = 0
    while number_prime < 10001:
        if is_prime(n):
            number_prime += 1
            yield n
        n += 1

def euler_7():
    prime = prime_gen()
    while True:
        try:
            answer = prime.next()
        except StopIteration:
            return answer

print "Answer: %s" % euler_7()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)    
