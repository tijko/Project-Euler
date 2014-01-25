## Find sum of all numbers where the factorials of its digit add up to itself ##

## Say 145 = 1! + 4! + 5! = 1 + 24 + 120 ##

import timeit
from math import factorial


start = timeit.default_timer()

def euler_34():
    return sum([i for i in xrange(3, 7 * factorial(9)) if 
                sum(map(factorial, map(int, str(i)))) == i])


print "Answer: %s" % euler_34()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
