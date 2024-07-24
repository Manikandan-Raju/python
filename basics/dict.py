import string
import pandas as pd

print([i for i in string.ascii_letters])

d = {j:i for i,j in enumerate(string.ascii_lowercase)}

print(d)

d = {**d,'yes':1}

l = [1,2,3]
l = [*l,4]
print(l)

s = 'manikandan'
print()
s= list(s)
s = pd.Series(s)
print(s.value_counts())
print(l[7:2:-1])