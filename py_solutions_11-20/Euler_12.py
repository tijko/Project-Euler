import math
import timeit


start = timeit.default_timer()

def euler_12():
    num = 1001
    divisors = 2 
    while True:
        tri = sum(xrange(1, num + 1))
        for i in xrange(2, int(math.sqrt(tri)) + 1):
            if tri % i == 0:
                divisors += 2
        if divisors > 500:
            return tri
        else:
            divisors = 2
            num += 1
    
print "Answer: %s" % euler_12()
stop = timeit.default_timer()
print ("Time: %f" % (stop - start))
