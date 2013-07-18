# How many different ways can 100 hundred be written by adding at least two numbers 

import timeit


start = timeit.default_timer()

def euler_76():
    ways = [0] * (100 + 1)
    ways[0] = 1
    for i in xrange(1, 100):
        for j in xrange(i, 101):
            ways[j] += ways[j - i]
    return ways[100]

print "Answer: %s" % euler_76()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)


