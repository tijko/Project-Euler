## sum of even fibonacci numbers below 4 million ? ##

import timeit


start = timeit.default_timer()

def Euler_2(limit):
    a1 = 1
    b1 = 1
    b2 = 0
    while b2 <= limit:
        b2 = a1 + b1
        a1 = b1
        b1 = b2
        if b2 % 2 == 0:
            yield b2

print "Answer: %s" % sum([i for i in Euler_2(4000000)])
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
