# square root of two -- how many iterations under 1001 contain a numerator with more digits than the denominator? 

import timeit


start = timeit.default_timer()

def euler_57():
    n = 3
    d = 2
    exp = [] 
    old_n = 1
    old_d = 1
    for i in xrange(1000):
        exp.append([n, d])
        new_n = (n * 2) + old_n 
        new_d = (d * 2) + old_d
        old_n = n
        old_d = d    
        n = new_n
        d = new_d
    return len([i for i in exp if len(str(i[0])) > len(str(i[1]))])

print "Answer: %s" % euler_57()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
