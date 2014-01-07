# square root of two -- how many iterations under 1001 contain a numerator with more digits than the denominator? 

import timeit


start = timeit.default_timer()

def numr_gen():
    prev_n = 1
    numerator = 3
    for _ in xrange(1001):
        yield numerator
        next_n = (numerator * 2) + prev_n
        prev_n = numerator
        numerator = next_n

def denom_gen():
    prev_d = 1
    denominator = 2 
    for _ in xrange(1001):
        yield denominator 
        next_d = (denominator * 2) + prev_d
        prev_d = denominator
        denominator = next_d

def euler_57():
    numr, denom = numr_gen(), denom_gen()
    num_digits = lambda n: len(str(n))
    return sum([1 for _ in xrange(1001) if num_digits(numr.next()) > num_digits(denom.next())])
        
print "Answer: %s" % euler_57()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
