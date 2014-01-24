# Sum of numbers that can be written as the sum of their fifth power. 

import timeit


start = timeit.default_timer()

def euler_30():
    fifth_pow = lambda x: x**5
    return sum([i for i in xrange(2, 1000000) if
                sum(map(fifth_pow, map(int, str(i)))) == i])

print "Answer: %s" % euler_30()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
