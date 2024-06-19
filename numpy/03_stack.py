import numpy as np


n1 = np.array([[1,2,3],
               [4,5,6]])


n2 = np.array([[1,2,3],
               [4,5,6]])

nh = np.hstack([n1,n2])
print(nh)

nv = np.vstack([n1,[1,2,3]])
print(nv)