x = 10
def fact(x):
     if x <=1:
        return 1
     else:
        return fact(x-1) * x

print(list(fact(i) for i in range(x) ))
