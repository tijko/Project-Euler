# Find the only pythagorean triplet that a + b + c = 1000 

import math
import timeit


start = timeit.default_timer()

def euler_9():
    for a in xrange(1, 3000):
        b = a + 1
        for b in xrange(b, 3000):
            if sum([a, b, (math.sqrt(a**2 + b**2))]) == 1000:
                return ("Answer: %s" % int((a * b * (math.sqrt(a**2 + b**2)))))
            elif sum([a, b, (math.sqrt(a**2 + b**2))]) > 1000:
                break

print 'Answer: %s' % euler_9()
stop = timeit.default_timer()
print 'Time: %f' % (stop - start)
