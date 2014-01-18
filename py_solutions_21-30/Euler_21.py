# Calculate the sum of all amicable pairs below 10000 

import timeit
import functools

start = timeit.default_timer()

def mod_zero(dividend, divisor):
    return True if dividend % divisor == 0 else False

def euler_21():
    amicable = set()
    for i in xrange(1, 10000):
        p1 = sum(filter(functools.partial(mod_zero, i), 
                   xrange(1, int(i / 2) + 1)))  
        p2 = sum(filter(functools.partial(mod_zero, p1), 
                        xrange(1, int(p1 / 2) + 1)))
        if p2 == i and i != p1: 
            amicable.add(i)
    return sum(amicable)


print "Answer: %s" % euler_21()     
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
