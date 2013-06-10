## Sum of numbers that can be written as the sum of their fifth power. ##

import timeit


start = timeit.default_timer()

def euler_30():
    canidates = (i for i in xrange(2, 1000000))
    total = 0
    while True:
        try:
            i = canidates.next()
            if sum(int(v)**5 for v in str(i)) == i:
                total += i
        except StopIteration:
            return total


print "Answer: %s" % euler_30()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
