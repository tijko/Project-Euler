# find the number sundays that fell on the first day of the month in between 1901 - 2000 

import timeit


start = timeit.default_timer()

def euler_19():
    years = xrange(1901, 2000) 
    answer = 0 
    weekday = 0  
    day_dict = {}
    for i in years: 
        if i % 4 == 0: 
            Feb = xrange(1, 30) 
        else: 
            Feb = xrange(1, 29) 
        Jan = Mar = May = Jul = Aug = Oct = Dec = xrange(1, 32)    
        Apr = Jun = Sep = Nov = xrange(1, 31) 
        year = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec] 
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
        count = 1 
        mos = 0 
        while mos < len(year): 
            for i in year[mos]: 
                day_dict[count] = week[weekday] 
                count += 1 
                weekday += 1 
                if weekday > 6: 
                    weekday = 0 
            if day_dict[1] == 'Sunday': 
                answer += 1 
            mos += 1 
            count = 1 
    return answer 

print "Answer: %s" % euler_19()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
