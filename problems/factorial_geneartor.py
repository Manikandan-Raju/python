import time


def fact_gen():
    i = 0
    fact = 1
    while True:
        if i <= 1:
            yield 1
        else:
            yield i * fact
            fact *= i
        i += 1


def fact(n):
    if n <=1:
        return 1
    else:
        return fact(n-1) * n


for i,v in enumerate(fact_gen()):
    print(i,v)
    time.sleep(0.5)
    print(i,fact(i))
    
