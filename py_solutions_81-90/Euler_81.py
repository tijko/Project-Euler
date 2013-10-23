#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Minimal path in a 80x80 matrix, going from top left node to bottom right node.
Moving only in the right and down direction.
'''

import timeit
import os

start = timeit.default_timer()

global edges
global traveled
global heap

path = os.getcwd().strip('py_solutions_81-90')
with open(path + 'euler_txt/matrix.txt') as f:
    grid = f.read()

edges = [[int(i) for i in v.split(',')] for v in grid.split('\r\n') if v]      
traveled = []

for i in range(80):
    row = ['inf'] * 80
    traveled.append(row)

x = y = 0
heap = [[y, x]]

def dijkstra(y, x):
    bounds = 80
    r_vertex = d_vertex = False
    if traveled[y][x] == 'inf':
        traveled[y][x] = curr = edges[y][x]
    else:
        curr = traveled[y][x]
    if y + 1 >= bounds and x + 1 >= bounds:
        return
    if y + 1 < bounds:
        d_vertex = curr + edges[y+1][x]
        if traveled[y+1][x] == 'inf':
            traveled[y+1][x] = d_vertex
        elif curr + edges[y+1][x] < traveled[y+1][x]:
            traveled[y+1][x] = d_vertex 
        else:
            d_vertex = False
    if x + 1 < bounds:
        r_vertex = curr + edges[y][x+1]
        if traveled[y][x+1] == 'inf':
            traveled[y][x+1] = r_vertex
        elif curr + edges[y][x+1] < traveled[y][x+1]:
            traveled[y][x+1] = r_vertex
        else:
            r_vertex = False
    if d_vertex and r_vertex:
        if d_vertex < r_vertex:
            heap.append([y, x+1])
            dijkstra(y+1, x) 
        else:
            heap.append([y+1, x])
            dijkstra(y, x+1)
    elif d_vertex:
        dijkstra(y+1, x)
    elif r_vertex:
        dijkstra(y, x+1)
    else:
        return    

while heap:
    y, x = heap.pop(0)
    dijkstra(y, x)         

stop = timeit.default_timer()
print "Answer: %d" % traveled[79][79]
print "Time: %f" % (stop - start)
