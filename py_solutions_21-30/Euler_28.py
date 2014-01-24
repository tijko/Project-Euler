# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import timeit


start = timeit.default_timer()

def grid(step, axis):
    total = step
    for i in xrange(len(axis)):
        step += axis[i]
        if step > axis[len(axis) - 1]:
            break
        total += step
    return total

 
def euler_28():
    diag = 3
    total = sum(map(lambda x: x**2, xrange(1, 1002, 2)))
    for i in range(10, 15, 2):
        total += grid(diag, xrange(i, 1002002, 8))
        diag += 2
    return total


print "Answer: %s" % euler_28()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
