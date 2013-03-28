## find the only pythagorean triplet that a + b + c = 1000 ##

import math
import timeit

start = timeit.default_timer()

def euler_9():
    triplet_range = range(1, 3000)
    b = 0
    for a in triplet_range:
        b = triplet_range.index(a) + 1
        while b < len(triplet_range):
            if a + b + (math.sqrt(a**2 + b**2)) == 1000:
                return ("Answer = %s | Triplet: A=%s, B=%s, C=%s" %  
                        (a * b * (math.sqrt(a**2 + b**2)), a, b, (math.sqrt(a**2 + b**2))))
            if a + b + (math.sqrt(a**2 + b**2)) > 1000:
                break
            b += 1

print euler_9()
stop = timeit.default_timer()
print 'Time: %s' % str(stop - start)
