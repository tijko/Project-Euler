# How many positive n-digit numbers exist which are also n'th powers?

import timeit


start = timeit.default_timer()

def euler_63():
    total = 0
    for n in xrange(1, 100):
        for i in xrange(1, 100):
            if len(str(i**n)) == n:
                total += 1    
    return total

print "Answer: %s" % euler_63()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)    
