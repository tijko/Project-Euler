## sum of all multiples of 3 and 5 below 1000? ##


print sum([i for i in xrange(1,1000) if i % 3 == 0 or i % 5 == 0])
