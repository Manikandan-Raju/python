import numpy as np

# NumPy fill helpers
# np.zeros creates an array filled with 0
zeros = np.zeros((5, 3))
print(zeros)

# np.ones creates an array filled with 1
ones = np.ones((2, 4), dtype=float)
print(ones)

# np.full creates an array filled with a specific value
full = np.full((3, 5), 13)
print(full)

# np.arange creates a sequence of numbers
arange = np.arange(20, 1, -2)
print(arange)

# np.linspace creates evenly spaced values between start and stop
linspace = np.linspace(0, 1, 5)
print(linspace)

# reshape changes the shape without changing the data order
reshape = np.arange(1, 21).reshape(4, 5)
print(reshape)

# np.random.randint generates random integers in a range
random = np.random.randint(1, 7, 20)
print(random)

# Pandas does not have pd.zeros / pd.ones / pd.random directly.
# Use NumPy arrays and wrap them in pandas if needed.
# Example:
# import pandas as pd
# df = pd.DataFrame(np.zeros((3, 4)))
# df = pd.DataFrame(np.ones((2, 5)))
# s = pd.Series(np.random.random(6))
