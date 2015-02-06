# sum of even fibonacci numbers below 4 million? 

from __future__ import print_function
import timeit


start = timeit.default_timer()
def euler_2():
    a, b = 0, 1
    while b <= 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            yield b
"""
def euler_2(t=0, n=2, ln=1):
    if n >= 4000000: return t
    elif n % 2 == 0: return euler_2(t + n, n + ln, n)
    return euler_2(t, n + ln, n)
"""

#print("Answer: {}".format(euler_2()))
print("Answer: {}".format(sum([i for i in euler_2()])))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
