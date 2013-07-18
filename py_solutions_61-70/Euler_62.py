# find the smallest cube that can be permutated to 5 other cubes 

import itertools
import timeit


start = timeit.default_timer()

def euler_62():
    cubes = [sorted([v for v in str(i**3)]) for i in xrange(10001)]
    for cube in cubes:
        if cubes.count(cube) == 5:
            return (cubes.index(cube)**3)

print "Answer: %s" % euler_62()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
