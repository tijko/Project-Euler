#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making 
use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it 
is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different 
target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can 
be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set 
of consecutive positive integers, 1 to n, can be obtained, giving your answer as 
a string: abcd.
'''

from __future__ import print_function
from itertools import combinations, permutations, zip_longest, product, chain 

import timeit

try:
    range = xrange
except NameError:
    pass

# all the possible bracket placements
brackets = ['({} {} {} {} {} {} {})', '({} {} {} {} {}) {} {}', 
            '(({} {} {}) {} {}) {} {}', '({} {} {}) {} ({} {} {})', 
            '{} {} ({} {} {} {} {})', '{} {} (({} {} {}) {} {})',
            '({} {} ({} {} {})) {} {}', '{} {} {} {} ({} {} {})', 
            '{} {} ({} {} ({} {} {}))', '{} {} ({} {} {}) {} {}', 
            '({} {} {}) {} {} {} {}']

operators = ('+', '-', '/', '*')
# set cartesian-product of operators (all possible equations).
operator_sets = list(product(operators, repeat=3))

def find_all_equation_solutions(digit_set_combination):
    # create all possible permutations of the combination
    digit_set_permutations = permutations(digit_set_combination)
    tracked_integers = set()
    for digit_set_permutation in digit_set_permutations:
        for operator_set in operator_sets:
            # zip_longest because of 4 digits and 3 operators
            # filling with a empty str.  these will format into brackets 
            eq_list = list(chain(*zip_longest(digit_set_permutation, 
                                              operator_set, fillvalue='')))
            for bracket in brackets:
                try:
                    # call eval on the bracket string to compute the equation
                    value = eval(bracket.format(*eq_list))
                except ZeroDivisionError:
                    pass 
                if value > 0 and value % 1 == 0:
                    tracked_integers.add(int(value))
    return tracked_integers

def euler_93():
    # all possible combinations of 4 digits
    digit_set_combinations = combinations(range(1, 10), 4)
    consecutive_high = 0
    high_set = ()
    for digit_set_combination in digit_set_combinations:
        integers = sorted(list(find_all_equation_solutions(digit_set_combination)))
        if not integers: continue
        for idx, integer in enumerate(integers, 1):
            if idx != integer: break
        if idx > consecutive_high:
            consecutive_high = idx
            high_set = digit_set_combination
    return ''.join(map(str, high_set))

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_93()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
