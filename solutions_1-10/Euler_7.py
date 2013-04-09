# What is the 10001st prime number?

import math
import timeit


start = timeit.default_timer()

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

def euler_7():
    answer = []
    inc = 0
    while len(answer) < 10001:
        if is_prime(inc):
            answer.append(inc)
        inc += 1
    return answer[len(answer) - 1]

print "Answer: %s" % euler_7()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
