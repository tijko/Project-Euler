# Find the largest palindrome number made from the product of two 3-digit numbers?

import itertools
import operator 
import timeit


start = timeit.default_timer()

def euler_4():
    canidates = itertools.combinations(xrange(100, 1000), 2)
    palindrome_check = lambda x: (str(operator.mul(*x)) ==  
                                  str(operator.mul(*x))[::-1])
    return max([operator.mul(*i) for i in canidates if palindrome_check(i)])

print "Answer: %s" % euler_4()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
