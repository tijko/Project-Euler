# Find the maximum total from top to bottom of the triangle below:

from __future__ import print_function

import os
import timeit


start = timeit.default_timer()

def euler_18():
    path = os.getcwd().strip('py_solutions_11-20')
    with open(path + '/euler_txt/triangle1.txt') as f:
        tri = [list(map(int, i.split())) for i in f.readlines()]
    row = col = total = 0
    while row < len(tri) - 2:
        total += tri[row][col]
        col += (1 if tri[row + 1][col + 1] + 
                max(tri[row + 2][col + 1], 
                    tri[row + 2][col + 2]) > 
                    tri[row + 1][col] + 
                max(tri[row + 2][col], 
                    tri[row + 2][col + 1]) else 0)
        row += 1
    total += (tri[row][col] + max(tri[row + 1][col], tri[row + 1][col + 1]))
    return total


print("Answer: {}".format(euler_18()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
