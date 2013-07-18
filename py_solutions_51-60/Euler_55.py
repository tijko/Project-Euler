# Lychrel Numbers 

import timeit


start = timeit.default_timer()

def euler_55():
    count = 0
    lychrel = 0
    for i in xrange(12, 10000):
        while count < 50: 
            reversi = ''.join([v for v in str(i)][::-1])
            palindrome = i + int(reversi) 
            count += 1 
            i = palindrome 
            if count == 50: 
                lychrel += 1 
            if [k for k in str(palindrome)] == [k for k in str(palindrome)][::-1]: 
                count = 50 
        count = 0 
    return lychrel

print "Answer: %s" % euler_55()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start) 
