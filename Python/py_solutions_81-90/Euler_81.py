#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Minimal path in a 80x80 matrix, going from top left node to bottom right node.
Moving only in the right and down direction.
'''

from __future__ import print_function

import timeit
import os


try:
    range = xrange
except NameError:
    pass


path = os.getcwd().strip('py_solutions_81-90')

with open(path + 'euler_txt/matrix.txt') as f:
    edges = [list(map(int, v.split(','))) for v in f.readlines()] 
    traveled = [['inf'] * 80 for _ in range(80)]

def euler_81():
    x = y = 0
    heap = [[y, x]]
    while heap:
        y, x = heap.pop(0)
        traverse(y, x, heap)         
    return traveled[79][79]

def traverse(y, x, heap):
    bounds = 80
    r_vertex = d_vertex = False
    if traveled[y][x] == 'inf':
        traveled[y][x] = curr = edges[y][x]
    else:
        curr = traveled[y][x]
    if y + 1 >= bounds and x + 1 >= bounds:
        return
    if y + 1 < bounds:
        d_vertex = y_edge(y, x, curr)
    if x + 1 < bounds:
        r_vertex = x_edge(y, x, curr)
    if d_vertex and r_vertex:
        if d_vertex < r_vertex:
            heap.append([y, x + 1])
            traverse(y + 1, x, heap) 
        else:
            heap.append([y + 1, x])
            traverse(y, x + 1, heap)
    elif d_vertex:
        traverse(y + 1, x, heap)
    elif r_vertex:
        traverse(y, x + 1, heap)

def y_edge(y, x, curr): 
    d_vertex = curr + edges[y+1][x]
    if traveled[y+1][x] == 'inf':
        traveled[y+1][x] = d_vertex
    elif d_vertex < traveled[y+1][x]:
        traveled[y+1][x] = d_vertex 
    else:
        d_vertex = False
    return d_vertex 

def x_edge(y, x, curr):
    r_vertex = curr + edges[y][x+1]
    if traveled[y][x+1] == 'inf':
        traveled[y][x+1] = r_vertex
    elif r_vertex < traveled[y][x+1]:
        traveled[y][x+1] = r_vertex
    else:
        r_vertex = False
    return r_vertex

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_81()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
