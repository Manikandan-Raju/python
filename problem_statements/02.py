# Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N.

import timeit
import time
import matplotlib.pyplot as plt
import random

random.seed(1)
l = [2,3,4,5,11]
n = 7

def get_pair(l,n):
    return next(((k,v) for i,k in enumerate(l) for v in (l[i:])  if k+v == n),None)

t = timeit.timeit('get_pair(l,n)', number=1000, globals = globals())
print(t)

length = [x for x in range(1,201)]

iterfibo_time = []
fibo_time = []

for i in length:
    # iterfibo's execution time
    l = [random.randint(0,i*3) for _ in range(i)]
    n = random.randrange(0,i*2)
    ts = time.time()
    get_pair(l,n)
    t = float(time.time() - ts)
    iterfibo_time.append(t)

# plt.plot(length, fibo_time)
plt.plot(length, iterfibo_time)
plt.show()