# Find the maximum total from top to bottom of the triangle below:

import os
import timeit

start = timeit.default_timer()

def euler_18(x):
   tot = 10
   row = 0
   position = 0
   tot += int(x[row][position])
   row += 1
   while row < len(x):
       if int(x[row][position]) > int(x[row][position+1]):
           tot += int(x[row][position])
       else:
           tot += int(x[row][position+1])
           position += 1
       row += 1
   return tot

with open(os.path.abspath('').strip('solutions_11-20') + 'euler_txt/triangle1.txt') as f:
    trck = []
    for line in f.readlines():
      trck.append(line.split())


print "Answer: %s" % euler_18(trck)
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
