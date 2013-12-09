## Sum of all Base-10 palindromes that are Base-2 palindromes too (under a million) ##

import timeit


start = timeit.default_timer()

def euler_36():
	return sum([i for i in xrange(1,1000000) if str(i)[::-1] == str(i) and bin(i).strip('0b') == bin(i).strip('0b')[::-1] and bin(i).strip('0b')[0] != '0' and bin(i)[len(bin(i))-1:] != '0'])

print "Answer: %s" % euler_36()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

