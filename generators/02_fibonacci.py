# Program to display the Fibonacci sequence up to n-th term

n1, n2 = 0, 1
for _ in range(n:=20):
    print(n1, end=" ")
    n1,n2 = n2,n1+n2