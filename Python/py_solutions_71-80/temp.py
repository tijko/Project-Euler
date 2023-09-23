#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find the least value of n for which p(n) is divisible by one million.

from __future__ import print_function

from functools import reduce

import math
import timeit

#counts = [(k,v) for k,v in collections.Counter(map(len, (partitions))).items()]
#print(sorted(counts, key=lambda x: x[0]))
import collections
#


try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

'''
    This can be done with one data-structure - List[List[Int]] or List[Set{Int}]
    Running as a While-Loop or a Recursive Function call

    input:
        limit               # Here a goal of being evenly divisible
        partition-count     # The current partitions counted
        partitions          # The partitions data-structure
    begin:
        if partition-count % limit == 0:
            return partition-count
        1.) Append 1 to every sub-list 
        2.) Increment +1

        the 2nd rule is only applied to a limited number...I am leaning
        on the case that it is a known index that from the start
        is made to increase either (or both)....for instance:
        going to index 5 [2,3] is going to need to be done like so

        - append 1 to the front -> [1,2,3]
        - inc +1 to idx-0       -> [3,3]
        - inc +1 to idx-1       -> [2,4]

        These 3 *alone* are crucial in created the next set...
        I do not know off the top of my head *if* these are
        the jump... it is close thats for sure....

[1]

[1,1], [2]

[1,1,1], [1,2], [3]

[1,1,1,1], [1,1,2], [1,3], [2,2], [4]

[1,1,1,1,1], [1,1,1,2], [1,1,3], [1,2,2], [1,4], [2,3], [5]

[1,1,1,1,1,1], [1,1,1,1,2], [1,1,1,3], [1,1,2,2], [1,1,4], [1,2,3], [2,2,2], [1,5], [2,4], [3,3], [6]

[1,1,1,1,1,1,1], [1,1,1,1,1,2], [1,1,1,1,3], [1,1,1,2,2], [1,1,1,4], [1,1,2,3], [1,2,2,2], [1,1,5], [1,2,4], [1,3,3], [2,2,3], [1,6], [2,5], [3,4], [7]
        
        (Going to be 2&5 ... 3&4 at the end....
   -------------------------------------------------------------------
   -------------------------------------------------------------------
   Rule 3.) has been deduced or rendered obselete.  There is no
            need to create a corner case or extra rule for something
            that is already baked into our algorithm.

            CREATE - sub_lists that have all the factorized integers
                     already baked into themselves.  Where going up
                     to what number has so many sub_lists.

            HEURISTIC - We already know that the integer N for the
                        target will need to at least be partitioned
                        a million times.  So by factoring out these
                        sub_lists


            CIRCLING-BACK - Having the first condition/rule/step of appending '1'
                            to the front of every sub-list.  This will carry *most*
                            of the cases.  To that end, I have now seen and believe
                            the next case will cover the now additional *addition*
                            case (or what I will refer to it as).

                            1. append '1' to the front of every sub-list.
                            2. iff the next sequential member is greater than
                               the current member than add +1 to the current
                               member

                            Keeping count of all of this members....As I go forth
                            this truly does feel as though I could complete it in
                            'Constant-Space' as well....using a factorization
                            method....to track whichever number we are at....

            RESOLVE - There has to be a way to do this using 'Constant-Space'
                      The factorization algorithm should be sufficient...
                      Where you are breaking down whatever integer into
                      the base factors (I forget if it has another name to it)
                      Anyways, yeah, just having the number itself, 
                      thinking jumping to just the difference from itself
                      and the last.  
    initialize:
        limit = 10**6
        partition-count = 0
        partitions = [[0]]
'''

def euler_78(partitions, count, limit):
    while True:
        next_lst = set()
        count += 1
        for sub_lst in partitions:
            curr = tuple([1] + sub_lst[:])
            next_lst.add(curr)
            length = len(sub_lst)
            curr = list(sub_lst)
            for idx,val in enumerate(curr[int(length/2):length-1]):
                if val < curr[idx+1]:
                    curr[idx] += 1
                    next_lst.add(tuple(curr))
                    break
        next_int = tuple([partitions[-1][0] + 1])
        next_lst.add(next_int)
        if len(next_lst) % limit == 0:
            return count
        print(count)
        partitions = list(map(list, next_lst))
    return

if __name__ == '__main__':
    limit = 10**6
    three = [[1,1,1], [1,2], [3]]
    four  = [[1,1,1,1], [1,1,2], [1,3], [2,2], [4]]
    five  = [[1,1,1,1,1], [1,1,1,2], [1,1,3], [1,2,2], [1,4], [2,3], [5]]
    six   = [[1,1,1,1,1,1], [1,1,1,1,2], [1,1,1,3], [1,1,2,2], [1,1,4], [1,2,3], [2,2,2], [1,5], [2,4], [3,3], [6]]
    print("Answer: %d" % euler_78(three, 3, limit)) 
    stop = timeit.default_timer()
    print("Time: %f" % (stop - start))
