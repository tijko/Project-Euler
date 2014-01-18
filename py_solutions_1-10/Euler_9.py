# Find the only pythagorean triplet that a + b + c = 1000 

import math
import timeit


start = timeit.default_timer()

def euler_9():
    triplet_range = xrange(1, 3000)
    for a in triplet_range:
        b = a + 1
        while b < len(triplet_range):
            if sum([a, b, (math.sqrt(a**2 + b**2))]) == 1000:
                return ("Answer: %s" % int((a * b * (math.sqrt(a**2 + b**2)))))
            elif sum([a, b, (math.sqrt(a**2 + b**2))]) > 1000:
                break
            b += 1

print 'Answer: %s' % euler_9()
stop = timeit.default_timer()
print 'Time: %f' % (stop - start)
