#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Minimal path in a 80x80 matrix, from top left node to bottom right node.
Moving up, down, left, or right directions.
'''

import timeit
import os
import time

start = timeit.default_timer()

global edges
global traveled
global heap

path = os.getcwd()

with open(path + '/matrix.txt') as f:
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
    r_vertex = d_vertex = u_vertex = l_vertex = False 
    if traveled[y][x] == 'inf':
        traveled[y][x] = curr = edges[y][x]
    else:
        curr = traveled[y][x]
    if x + 1 >= bounds and y + 1 >= bounds: 
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
    if y - 1 >= 0:  
        u_vertex = curr + edges[y-1][x]
        if traveled[y-1][x] == 'inf':
            traveled[y-1][x] = u_vertex
        elif curr + edges[y-1][x] < traveled[y-1][x]:
            traveled[y-1][x] = u_vertex
        else:
            u_vertex = False

    if x - 1 >= 0:
        l_vertex = curr + edges[y][x-1]
        if traveled[y][x-1] == 'inf':
            traveled[y][x-1] = l_vertex
        elif curr + edges[y][x-1] < traveled[y][x-1]:
            traveled[y][x-1] = l_vertex
        else:
            l_vertex = False

    mvs = {d_vertex:'d_vertex',
           r_vertex:'r_vertex',
           u_vertex:'u_vertex',
           l_vertex:'l_vertex'
          }
    if any(mvs):
        mvs = {k:v for k,v in mvs.items() if k}
        next_mv = min(mvs)
        heap_mv = mvs.values()
        if mvs[next_mv] == 'd_vertex':
            if 'r_vertex' in heap_mv:
                heap.append([y,x+1])
            if 'u_vertex' in heap_mv:
                heap.append([y-1,x])
            if 'l_vertex' in heap_mv:
                heap.append([y,x-1])
            dijkstra(y+1, x)
        elif mvs[next_mv] == 'r_vertex':
            if 'd_vertex' in heap_mv:
                heap.append([y+1,x])
            if 'u_vertex' in heap_mv:
                heap.append([y-1,x])
            if 'l_vertex' in heap_mv:
                heap.append([y,x-1])
            dijkstra(y, x+1)
        elif mvs[next_mv] == 'u_vertex':
            if 'd_vertex' in heap_mv:
                heap.append([y+1,x])
            if 'r_vertex' in heap_mv:
                heap.append([y,x+1])
            if 'l_vertex' in heap_mv:
                heap.append([y,x-1])
            dijkstra(y-1,x)
        else:
            if 'd_vertex' in heap_mv:
                heap.append([y+1,x])
            if 'r_vertex' in heap_mv:
                heap.append([y,x+1])
            if 'u_vertex' in heap_mv:
                heap.append([y-1,x])
            dijkstra(y,x-1)
    else:
        return    

while heap:
    y, x = heap.pop(0)
    dijkstra(y, x)      

stop = timeit.default_timer()
print "Answer: %d" % traveled[79][79]
print "Time: %f" % (stop - start)


