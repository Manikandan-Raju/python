
def fact(max):
    """Yield factorials from 0! up to (max - 1)!.

    This version keeps a running product so each factorial is built from the
    previous one instead of recomputing the full product every time.
    """
    result = 1
    for val in range(max):
        # At the start of each loop, `result` holds `val!`.
        yield result
        result *= val + 1


# print(list(fact(10)))

def fib(max):
    result = 0
    last = 1
    for i in range(max):
        yield result
        old_result = result
        result = result + last
        last = old_result





print(list(fib(10)))







def fact(n):
    if n <=1:
        return 1
    else:
        return fact(n-1) * n
    
def si(n):
    last1 = last2 = 1
    i = 0
    s = result = 1
    for i in range(n+1):
        if i <= 1:
            s = 1
        else:
            result = last1 + last2
        last2, last1 = last1, result
        if i >= n:  
            s = result
    return s
        
    
print([si(i) for i in range(10)])