'''
Write a program to check and return the pairs of a given array A 
whose sum value is equal to a target value N.
'''
A = [1, 2, 40, 3, 9, 4, 6, 5 ,4]
N = 7

seen = set()
for i in A:
    
    x = N - i
    if x in seen:
        print(x,i)
    seen.add(i)

