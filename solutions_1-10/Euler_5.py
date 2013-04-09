# what is the smallest number that can be divided evenly by all the numbers from 1-20 ?  

import timeit


start = timeit.default_timer()

def euler_5():
    count = 20
    divs = [i for i in xrange(1, 20 + 1)]
    while True:
        for i in divs:
            if count % i != 0:
                count += 20
                break
            if i == 20:
                return count

print "Answer: %s" % euler_5()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
