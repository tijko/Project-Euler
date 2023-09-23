# find the number sundays that fell on the first day of the month in between 
# 1901 - 2000. 

from __future__ import print_function

import timeit
from itertools import cycle

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_19(start, stop):
    leap_yr = range(1, 30)
    weekday = cycle(range(7))
    for i in range(start, stop):
        Feb = range(1, 29) if i % 4 != 0 else leap_yr
        Jan = Mar = May = Jul = Aug = Oct = Dec = range(1, 32)    
        Apr = Jun = Sep = Nov = range(1, 31) 
        year = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec] 
        yield sum([1 for mos in range(12) if 
                   list(zip(year[mos], weekday))[0] == (1, 6)])


print("Answer: {}".format(sum([sunday for sunday in euler_19(1901, 2000)])))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
