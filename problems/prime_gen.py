import time

def prime_gen():
    i = 0
    while True:
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                yield i 
        i +=1


for i in prime_gen():
    print(i)