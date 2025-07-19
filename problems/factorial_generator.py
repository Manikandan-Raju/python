import time


def fact_gen():
    i = 0
    fact = 1
    while True:
        if i == 0:
            yield 1
        else:
            fact *= i
            yield fact
        i += 1


def fact(n):
    if n <= 1:
        return 1
    else:
        return fact(n-1) * n



for i, v in zip(range(10), fact_gen()):
    print(i, v)
    time.sleep(0.5)
    print(i, fact(i))
    
