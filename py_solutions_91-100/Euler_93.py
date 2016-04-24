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
from itertools import combinations, permutations, zip_longest, product 

import timeit

try:
    range = xrange
except NameError:
    pass


def euler_93():
    digit_set_combinations = combinations(range(1, 10), 4)
    operators = ('+', '-', '/', '*')
    operator_sets = list(product(operators, repeat=3))
    brackets = ['({} {} {} {} {} {} {})', '({} {} {} {} {}) {} {}', 
                '(({} {} {}) {} {}) {} {}', '({} {} {}) {} ({} {} {})', 
                '{} {} ({} {} {} {} {})', '{} {} (({} {} {}) {} {})',
                '({} {} ({} {} {})) {} {}', '{} {} {} {} ({} {} {})', 
                '{} {} ({} {} ({} {} {}))', '{} {} ({} {} {}) {} {}', 
                '({} {} {}) {} {} {} {}']
    consecutive_high = 0
    high_set = ()
    for digit_set_combination in digit_set_combinations:
        digit_set_permutations = permutations(digit_set_combination)
        tracked_integers = set()
        for digit_set_permutation in digit_set_permutations:
            for operator_set in operator_sets:
                eq_list = [d for o in zip_longest(digit_set_permutation, 
                           operator_set) for d in o if d]
                for bracket in brackets:
                    try:
                        value = eval(bracket.format(*eq_list))
                    except ZeroDivisionError:
                        pass 
                    if value > 0 and value % 1 == 0:
                        tracked_integers.add(int(value))
        integers = sorted(list(tracked_integers))
        idx = 0
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
