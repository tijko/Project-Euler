# Find the smallest integer n -- where n2, n3, n4, n5, n6 all contain the same digits but, in different order ##

import timeit


start = timeit.default_timer()

def euler_52():
    permute = [i for i in xrange(1000, 200000) if set(str(i * 2)) == set(str(i * 4)) == set(str(i * 3)) == set(str(i * 5)) == set(str(i * 6)) == set(str(i))]
    return permute[0]

print "Answer: %s" % euler_52()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
