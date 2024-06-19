import time


def fibonacci_generator():
    i = 0
    last1 = last2 = 1
    while True:
        if i <= 1:
            yield 1
        else:
            yield last1 + last2
            new2 = last1 + last2
            last1 = last2
            last2 = new2
        i += 1
        

for i in fibonacci_generator():
    print(i)
    time.sleep(0.1)
