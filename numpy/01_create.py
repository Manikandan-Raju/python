import numpy as np

numbers = np.array([2,3,5,7,11])
print("numbers :",numbers)

#type
print("type : ",type(numbers))

#multi-dimension
print(np.array([[1,2,3],[4,5,6]]))

# dtype
print("dtype : ",numbers.dtype)

n = np.array([[1,2,3],[4,5,6],[7,8,9]])
# n-dimension
print("n-dimension : ",n.ndim)

# shape
print("shape : ",n.shape)

# size
print("size : ",n.size)