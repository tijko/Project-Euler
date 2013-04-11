# what is the sum of the digits 2**1000 ? 

import timeit


start = timeit.default_timer()

def euler_16():
    return sum([int(i) for i in str(2**1000)])

print "Answer: %s" % euler_16()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
