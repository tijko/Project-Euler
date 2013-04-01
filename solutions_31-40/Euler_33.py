## trivial example = 30/50 = 3/5 ##
## non-trivial example = 49/98 = 4/8 ##

## There are 4 non-trivial types of these fractions < 1 and both numerator and denominator contain  two digits ##
## find the the product of the four in its lowest common terms, what is the denominator? ##

import timeit


start = timeit.default_timer()

def euler_33():
    n = xrange(10, 100)
    d = xrange(10, 100)
    fract = []
    fin_n = 1
    fin_d = 1
    for j in range(len(n)):
        for i in d:
            if n[j]/i < 1:
                for v in str(n[j]):
                    if str(n[j]).count(v) == 1 and str(i).count(v) == 1:
                        new_n = str(n[j]).replace(v, '')
                        new_d = str(i).replace(v, '')          
                        if int(new_n) and int(new_d) > 0:
                            if float(new_n)/int(new_d) == float(n[j])/i and n[j] % 10 != 0:
                                fract.append([n[j], i])       
    for i in fract:   
        fin_n *= i[0]
    for i in fract:
        fin_d *= i[1]
    n_lcms = [i for i in range(2, fin_n + 1) if fin_d % i == 0 and fin_n % i == 0]
    return fin_d/n_lcms[len(n_lcms)-1]    
    

print "Answer: %s" % euler_33()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)

