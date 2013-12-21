# find the sum of the digits in !100 ? 

import math
import timeit


start = timeit.default_timer()

def euler_20():
    return sum(map(int, str(math.factorial(100))))

print "Answer: %s" % euler_20()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

