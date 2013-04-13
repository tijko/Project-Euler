# Diophantine equation 

import timeit
import math


start = timeit.default_timer()

def euler_66():
    canidates = [i for i in xrange(1, 1001) if i**0.5 % 1 != 0]
    high_x = 0
    high_D = 0
    for canidate in canidates:
        const_a = math.floor(math.sqrt(canidate))
        m0 = const_a
        d0 = (canidate - (m0**2)) / 1
        a0 = int((const_a + m0) / d0)
        x0 = const_a
        y0 = 1
        x1 = x0 * a0 + 1
        y1 = y0 * a0
        m0 = (d0 * a0) - m0
        d0 = (canidate - (m0**2)) / d0
        a0 = int((const_a + m0) / d0)
        k = x1**2 - canidate * y1**2
        if k == 1:
            if x1 > high_x:
                high_x = x1
                high_D = canidate
        x2 = x1 * a0 + x0
        y2 = y1 * a0 + y0
        while k != 1:
            x0 = x1
            y0 = y1
            x1 = x2
            y1 = y2
            m1 = (d0 * a0) - m0
            d1 = (canidate - (m1**2)) / d0
            a1 = (const_a + m1) / d1
            a0 = long(a1)
            d0 = d1
            m0 = m1
            x2 = long(x1) * a0 + long(x0)
            y2 = long(y1) * a0 + long(y0)
            k = x2**2 - canidate * y2**2
            if k == 1:
                if x2 > high_x:
                    high_x = x2
                    high_D = canidate
    return high_D


print "Answer: %s" % euler_66()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

