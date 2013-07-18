# Find the highest sum of a number's digits for numbers a**b while a and b < 100 

import timeit


start = timeit.default_timer()

def euler_56():
    digits = list() 
    powers = [i for i in xrange(1, 100)]
    for v in xrange(len(powers)):
        for i in powers:
            digits.append(i**v)
    return max([sum([int(v) for v in str(i)]) for i in digits])

print "Answer: %s" % euler_56()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
