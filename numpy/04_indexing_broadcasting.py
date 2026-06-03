# 04_indexing_broadcasting.py
# Important NumPy concepts: indexing, slicing, boolean masks, and broadcasting.

import numpy as np

arr = np.arange(12).reshape(3, 4)
print('Array:')
print(arr)

print('Second row:', arr[1])
print('Column 2:', arr[:, 2])

mask = arr % 2 == 0
print('Even mask:')
print(mask)
print('Even values:', arr[mask])

# Broadcasting example: add a 1D array to each row of a 2D array.
row_add = np.array([1, 2, 3, 4])
print('Broadcasted sum:')
print(arr + row_add)
