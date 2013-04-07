# magic 5-gon ring 

import itertools
import timeit


start = timeit.default_timer()

def euler_68():
    rings = [i for i in itertools.combinations(xrange(1, 11), 3)]
    rings = [i for j in [n for n in [itertools.permutations(v) for v in rings]] for i in j]
    pos = 1
    h = list()
    magic_gon = list()
    cycle = [[i] * 10 for i in range(720)]
    cycle = [i for j in cycle for i in j]
    for c in cycle:
        for i in rings:
            if (sum(i) == sum(rings[c]) and 
                rings[c][0] < i[0] and 
                rings[c][2] == i[1] and 
                i[0] not in rings[c]):
                h.append(rings[c])
                h.append(i)
                for j in rings:
                    if pos > len(h) - 1:
                        pos = 1
                        break
                    if (sum(h[pos]) == sum(j) and 
                        h[0][0] < j[0] and 
                        h[pos][2] == j[1] and 
                        j[0] not in h[pos] and 
                        h[pos][0] not in j and 
                        h[0][0] not in j):
                        canidate = ''.join([str(e) for d in h for e in d])
                        if (j[0] not in [n[0] for n in h] and 
                            str(j[0]) not in canidate):
                            h.append(j)
                            pos += 1
            if len(h) >= 4:
                if (h not in magic_gon and 
                    set(range(1, 11)) == set([t for r in h for t in r])):
                    magic_gon.append(h)
            h = list()
    magic_gon = [''.join([str(i) for v in k for i in v]) for k in magic_gon]
    return max([int(i) for i in magic_gon if len(i) == 16]) 

print "Answer: %s" % euler_68()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
