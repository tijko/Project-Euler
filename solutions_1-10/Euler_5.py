## what is the smallest number that can be divided evenly by all the numbers from 1-20 ? ## 
import timeit


start = timeit.default_timer()

def euler_5():
    pos = 0
    count = 20 
    divs = [i for i in range(1, 20 + 1)]
    while pos != 20:
        for i in divs:
            if count % i != 0:
                count += 1
                pos = 0
                break
            if count % i == 0:
                pos += 1
            if pos == 20:
                return count
                    

print euler_5()
stop = timeit.default_timer()
print stop - start
