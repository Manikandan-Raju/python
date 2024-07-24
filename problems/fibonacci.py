# Program to display the Fibonacci sequence up to n-th term

n1, n2 = 0, 1
for _ in range(n:=20):
    print(n1, end=" ")
    n1,n2 = n2,n1+n2
    
def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x-1) + fib(x-2)


print(list(fib(i) for i in range(10) ))