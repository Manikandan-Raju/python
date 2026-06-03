# 05_random.py
# Demonstrates NumPy random number generation and seeding.

import numpy as np

np.random.seed(0)
print('Random integers:', np.random.randint(1, 10, size=5))
print('Random floats:', np.random.random(5))

print('Random normal samples:')
print(np.random.randn(3, 3))

print('Shuffle example:')
a = np.arange(10)
np.random.shuffle(a)
print(a)
