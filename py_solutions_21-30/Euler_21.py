## calculate the sum of all amicable pairs below 10000 ##

import timeit

start = timeit.default_timer()


def euler_21():
    amicable = []
    first_sum = 0
    second_sum = 0
    for i in xrange(1, 10000):
        for k in xrange(1, int(i/2) + 1): 
            if i % k == 0: 
                first_sum += k 
        for v in xrange(1, int(first_sum/2) + 1): 
            if first_sum % v == 0: 
                second_sum += v 
        if second_sum == i and i != first_sum and i not in amicable: 
            amicable.append(i) 
        first_sum = 0 
        second_sum = 0 
    return sum(amicable)


print "Answer: %s" % euler_21()     
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
