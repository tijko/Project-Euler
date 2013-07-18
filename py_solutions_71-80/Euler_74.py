# factorial of each digit of a number to sequence 
# all numbers under a million max have 60 length sequence 

import math
import timeit


start = timeit.default_timer()

def euler_74():
    total = 0
    chain = list()
    for n in xrange(1, 1000001):
        if len(chain) >= 60:
            total += 1
        chain = [n]
        pos = 0    
        while True:
            next_term = sum([math.factorial(int(v)) for v in [j for j in str(chain[pos])]])
            if set(chain).intersection([next_term]):
                break
            chain.append(next_term)
            pos += 1
            if len(chain) >= 60:
                break
    return total

print "Answer: %s" % euler_74()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
                
