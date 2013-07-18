# Find the least value of n for which p(n) is divisible by one million.

import timeit
import sys


start = timeit.default_timer()

sys.setrecursionlimit(5000)

def pent(n):
    return int((0.5 * n) * ((3 * n) - 1))

def gen_pent(n):
    return pent(int(((-1)**(n + 1)) * (round((n + 1) / 2))))

partitions = {0:1, 1:1, 2:2, 3:3, 4:5, 5:7, 6:11, 7:15, 8:22, 9:30, 10:42}

def partition(n):
    if n in partitions:
        return partitions[n]
    total, sign, i = 0, 1, 1
    while n - gen_pent(i) >= 0:
        sign = (-1)**int((i - 1) / 2)
        total += sign * partition(n - gen_pent(i))
        i += 1
        partitions[n] = total
    return total

def euler_78():
    n = 2001
    while partition(n) % 1000000 != 0:
        n += 1
    return n

print "Answer: %s" % euler_78()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
