#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A natural number, N, that can be written as the sum and product of a given set
of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum
number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a
minimal product-sum number. The minimal product-sum numbers for sets of size,
k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is
4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for
2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
'''

from __future__ import print_function, division

from math import sqrt
from collections import defaultdict

import timeit


factor_dict = defaultdict(list)
min_prod_sum = {}

def is_prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def euler_88(limit):
    n = 2
    while len(min_prod_sum) < 11999:
        if not is_prime(n):
            find_factors(n)
        n += 1
    return sum({min_prod_sum[i] for i in min_prod_sum})

def check_current_min(n, lst):
    lst_sum = sum(lst)
    candidate = (n - lst_sum) + len(lst)
    if candidate > 12000 or candidate < 2:
        return
    current = min_prod_sum.get(candidate)
    if current is None or n < current:
        min_prod_sum[candidate] = n

def int_to_list_combo(n, n_list, f, flst):
    for factor in flst:
        lst = sorted([f] + factor)
        if lst not in n_list:
            n_list.append(lst)
            check_current_min(n, lst)

def create_factor_combos(n, f1, f2):
    # once formed check each list for sum and length
    f1_factors = factor_dict.get(f1) or []
    f2_factors = factor_dict.get(f2) or []
    n_list = factor_dict[n]
    n_list.append([f1, f2])
    check_current_min(n, [f1, f2])
    int_to_list_combo(n, n_list, f1, f2_factors)
    int_to_list_combo(n, n_list, f2, f1_factors)
    for factor1 in f1_factors:
        for factor2 in f2_factors:
            lst = sorted(factor1 + factor2)
            if lst not in n_list:
                n_list.append(lst)
                check_current_min(n, lst)

def find_factors(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            f2 = int(n / i)
            create_factor_combos(n, i, f2)

if __name__ == "__main__":
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_88(12000)))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
