# Lychrel Numbers 

import timeit


start = timeit.default_timer()

def euler_55():
    lychrel = 0
    for i in xrange(12, 10000):
        for l in xrange(51):
            palindrome = i + int(str(i)[::-1]) 
            i = palindrome 
            if str(palindrome) == str(palindrome)[::-1]:
                break
        if l == 50:
            lychrel += 1
    return lychrel

print "Answer: %s" % euler_55()
stop = timeit.default_timer()
print "Time: %f" % (stop - start) 
