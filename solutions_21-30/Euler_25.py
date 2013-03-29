## what is the first fibonacci number to have 1000 digits in it? ##

import timeit


start = timeit.default_timer()

def euler_25():
    a1 = 1
    count = 2
    b1 = 1
    while True:
        b2 = a1 + b1
        a1 = b1
        b1 = b2
        count += 1
        if len(str(b2)) >= 1000:
            return count


print "Answer: %s" % euler_25()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
