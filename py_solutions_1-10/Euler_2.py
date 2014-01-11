# sum of even fibonacci numbers below 4 million? 

import timeit


start = timeit.default_timer()

#def euler_2():
#    a1 = 1
#    b1 = 1
#    b2 = 0
#    limit = 4000000
#    while b2 <= limit:
#        b2 = a1 + b1
#        a1 = b1
#        b1 = b2
#        if b2 % 2 == 0:
#            yield b2

def euler_2(t=0, n=2, ln=1):
    if n >= 4000000:
        return t 
    if n % 2 == 0:
        return euler_2(t + n, n + ln, n)
    return euler_2(t, n + ln, n)

print "Answer: %s" % euler_2() 
#print "Answer: %s" % sum([i for i in euler_2()])
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
