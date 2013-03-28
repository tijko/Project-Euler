# -*- coding: utf-8 -*-

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

import timeit

start = timeit.default_timer()

new = ''
new = new + 'one' * 191 
new = new + 'two' * 190
new = new + 'three' * 190
new = new + 'four'  * 190
new = new + 'five'  * 190
new = new + 'six'  * 190
new = new + 'seven'  * 190
new = new + 'eight'  * 190
new = new + 'nine' * 190
new = new + 'ten' * 10
new = new + 'eleven' * 10
new = new + 'twelve' * 10
new = new + 'thirteen' * 10
new = new + 'fourteen' * 10
new = new + 'fifteen' * 10
new = new + 'sixteen' * 10
new = new + 'seventeen' * 10
new = new + 'eighteen' * 10
new = new + 'nineteen' * 10
new = new +'twenty' * 100
new = new + 'thirty' * 100
new = new + 'forty' * 100
new = new + 'fifty' * 100
new = new + 'sixty' * 100
new = new + 'seventy' * 100
new = new + 'eighty' * 100
new = new + 'ninety' * 100
new = new + 'hundredand' * 891
new = new + 'hundred' * 9
new = new + 'thousand' * 1

print "Answer: %s" % len(new)
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
