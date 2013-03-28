## what is the sum of the digits 2**1000 ? ##

import timeit

start = timeit.default_timer()

print "Answer: %s" % sum([int(i) for i in str(2**1000)])
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
