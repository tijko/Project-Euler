# find the number sundays that fell on the first day of the month in between 1901 - 2000 

import timeit
from itertools import cycle


start = timeit.default_timer()

def euler_19():
    sundays = 0 
    weekday = cycle(xrange(7))
    for i in xrange(1901, 2000):
        if i % 4 == 0: 
            Feb = xrange(1, 30) 
        else: 
            Feb = xrange(1, 29) 
        Jan = Mar = May = Jul = Aug = Oct = Dec = xrange(1, 32)    
        Apr = Jun = Sep = Nov = xrange(1, 31) 
        year = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec] 
        sundays += sum([1 for mos in xrange(12) if 
                        zip(year[mos], weekday)[0] == (1, 6)]) 
    return sundays 

print "Answer: %s" % euler_19()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
