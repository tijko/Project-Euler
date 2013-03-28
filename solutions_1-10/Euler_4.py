## find the largest palindrome number made from the product of two digit numbers ? ##

import itertools

canidates = [i for i in xrange(100,1000)]

canidates = [i for i in itertools.combinations(canidates, 2)]

current_high = 0

for canidate in canidates:
    new = canidate[0] * canidate[1]
    if str(new)[::-1] == str(new) and new > current_high:
        current_high = new

print current_high
