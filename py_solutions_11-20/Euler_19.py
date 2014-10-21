# find the number sundays that fell on the first day of the month in between 
# 1901 - 2000. 

import timeit
from itertools import cycle


start = timeit.default_timer()

def euler_19(start, stop):
    leap_yr = xrange(1, 30)
    weekday = cycle(xrange(7))
    for i in xrange(start, stop):
        Feb = xrange(1, 29) if i % 4 != 0 else leap_yr
        Jan = Mar = May = Jul = Aug = Oct = Dec = xrange(1, 32)    
        Apr = Jun = Sep = Nov = xrange(1, 31) 
        year = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec] 
        yield sum([1 for mos in xrange(12) if 
                   zip(year[mos], weekday)[0] == (1, 6)])


print "Answer: %s" % sum([sunday for sunday in euler_19(1901, 2000)])
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
