#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Each of the six faces on a cube has a different digit (0 to 9) written on it;
the same is done to a second cube. By placing the two cubes side-by-side in
different positions we can form a variety of 2-digit numbers.

In fact, by carefully choosing the digits on both cubes it is possible to
display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49,
64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so
that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for
all nine square numbers to be displayed; otherwise it would be impossible to
obtain 09.

In determining a distinct arrangement we are interested in the digits on each
cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the
last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the
purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square
numbers to be displayed?
'''

from __future__ import print_function
from itertools import combinations, product

import timeit


def euler_90():
    squares = {'01', '04', '09', '16', '25', '36', '49', '64', '81'}
    all_cubes = combinations(map(str, range(10)), 6)
    all_cube_pairs = [map(set, pair) for pair in  combinations(all_cubes, 2)]
    count = 0
    six_nine = {'6', '9'}
    for pair in all_cube_pairs:
        s1, s2 = pair
        s1 = s1 | six_nine if s1 & six_nine else s1
        s2 = s2 | six_nine if s2 & six_nine else s2
        s1_prod = {''.join(i) for i in product(s1, s2)}
        s2_prod = {''.join(i) for i in product(s2, s1)}
        if squares & (s1_prod | s2_prod) == squares:
            count += 1
    return count

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_90()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
