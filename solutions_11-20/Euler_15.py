## find all paths in 20 X 20 grid ##

import math
import timeit

start = timeit.default_timer()

new = math.factorial(40)

print "Answer: %s" % str(new/(math.factorial(20)*math.factorial(20)))
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
