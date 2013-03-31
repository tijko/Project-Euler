## Find sum of all numbers where the factorials of its digit add up to itself ##
## Say 145 = 1! + 4! + 5! = 1 + 24 + 120 ##

import timeit
import math


start = timeit.default_timer()

def euler_34():
    answers = []
    for i in xrange(3, 7 * math.factorial(9)):
        if sum([math.factorial(int(v)) for v in str(i)]) == i:
            answers.append(i)
    return sum(answers)


print "Answer: %s" % euler_34()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
