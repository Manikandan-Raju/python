import numpy as np
import pandas as pd

arr = np.array([1,2,8.5])
arr = np.array(["a",2])
d = {1:2,2:3,3:4}
a = [3]
d ={k:v for k,v in d.items() if k not  in a}
l = [1,2,3,4,5]
lis = [a*a  for a in l if 10< a*a <30 ]
l = list(filter(lambda x: 10<x<30,map(lambda x: x**2 ,l)))
l = list(range(1,6))
np.random.seed(1)

df = pd.DataFrame(np.random.randint(0,9,(5,4)))
print(df)

s = pd.Series(np.random.randint(0,9,5))
print(s)

df.loc[:,df.columns.size] = s
print(df)

df.loc[df.index.size] = s
print(df)

print((df[2].diff(1) == -1) & (df[2] == 4) & (df[2].shift(1) == 5))
print((df[2].diff(1)))


s = pd.DataFrame(np.random.randn(3,3))
print(s)