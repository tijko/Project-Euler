## find the sum of the digits in !100 ? ##

import math
import timeit

start = timeit.default_timer()

print "Answer: %s" % sum([int(i) for i in str(math.factorial(100))])
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)

