# Write a Python function that takes a string and a character as input and 
# returns the count of occurrences of that character in the string.


def count(s):
    d = {k:0 for k in s }
    d = {k:v+1 for k,v in d.items() if k in s}
    return [i for i in d if d[i] == max(d.values())]

count('manikandan')

#find max

l = [5,4,6,46,46,6,4564,4645,654,654,6,4]

max = l[0]

for i in l:
    if i > max:
        max = i


# Write a Python function to calculate the power of a given number using recursion.


def pow(n,e):
    if e == 0:
        return 1
    else:
        return pow(n,e-1) * n

p = pow(2,10)
print(p)
        

