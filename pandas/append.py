import pandas as pd
import numpy as np
import random
import string
np.random.seed(1)
a = np.random.randint(1,6,5)
print(a)


# a =np.vstack([a,np.array([32,2])])
# print(a)

s= pd.Series(a)
print(s)
s[10] = 7
print(s)

d = {k:v for k,v in   zip(string.ascii_lowercase, np.arange(1,26).reshape(5,5))  }
print(d)

df = pd.DataFrame(d)

print(df)

c = df.loc[1,'a':'c']

print(c)


print(df)

df =  df.sort_values(['a','b'])

print(df)
df =  df.drop('c',axis =1)


print(df)



# print(df[df['d']> 16])

# print(df.query('d > 16 and e < 24'))


print(df.loc[df['a']> 2,df.loc[1]>7])

