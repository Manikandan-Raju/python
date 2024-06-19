x = 10
def fact(x):
     if x <=1:
        return 1
     else:
        return fact(x-1) * x


def fib(x):
        if x <= 1:
            return x
        else:
            return fib(x-1) + fib(x-2)


print(list(fib(i) for i in range(x) ))
print(list(fact(i) for i in range(x) ))
