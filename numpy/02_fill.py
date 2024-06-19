import numpy as np


zeros = np.zeros((5,3))
print(zeros)

ones = np.ones((2,4),dtype=float)
print(ones)

full = np.full((3,5),13)
print(full)


arange = np.arange(20,1,-2)
print(arange)

linspace = np.linspace(0,1,5)
print(linspace)

reshape = np.arange(1,21).reshape(4,5)
print(reshape)

random = np.random.randint(1,7,20)
print(random)