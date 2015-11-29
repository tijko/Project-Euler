# maximum set of answers for triangle with perimeter <= 1000 

# Ex: perimeter = 120 sides = {30,40,50}, {32,48,52}, {24,45,51} 
# peri = range(4,1001) | a < b < c | a**2 + b**2 == c**2 

# first integral perimeter triangle [3,4,5] = 12 

import timeit
import math
import collections
import itertools


start = timeit.default_timer()

def euler_39():
    triangle_sums = []
    for x, i in itertools.product(xrange(999), xrange(3, 1001)):
        triangle = math.sqrt(x**2 + i**2)
        if not triangle.is_integer(): continue 
        triangle_sum = sum([x, i, triangle])
        if triangle_sum <= 1000:
            triangle_sums.append(triangle_sum)
    max_triangle_set = collections.Counter(triangle_sums)
    return max_triangle_set.most_common()[0][0]

print "Answer: %s" % euler_39()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

