## maximum set of answers for triangle with perimeter <= 1000 ##

# Ex: perimeter = 120 sides = {30,40,50}, {32,48,52}, {24,45,51} ##
# peri = range(4,1001) | a < b < c | a**2 + b**2 == c**2 ##

# first integral perimeter triangle [3,4,5] = 12 ##

import timeit
import math


start = timeit.default_timer()

def euler_39():
    answer = list()
    for x in xrange(999):
        for i in xrange(3, 1001):
            if (str(math.sqrt(x**2 + i**2))[::-1][:1] == '0' and 
                sum([x, i, math.sqrt(x**2 + i**2)]) <= 1000):
                answer.append(sum([x, i, math.sqrt(x**2 + i**2)]))
    return int([i for i in answer if  
                max([answer.count(v) for v in answer]) == answer.count(i)][0])



print "Answer: %s" % euler_39()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)

