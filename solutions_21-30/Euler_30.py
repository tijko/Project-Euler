## Sum of numbers that can be written as the sum of their fifth power. ##

import timeit


start = timeit.default_timer()

def euler_30():
    trial = [str(i) for i in range(2,1000000)]
    total = 0
    answer = []
    for i in trial:
        for v in i:
            total += int(v)**5
        if total == int(i):
            answer.append(int(i))
        total = 0
    return sum(answer)


print "Answer: %s" % euler_30()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
