import numpy as np
import pandas as pd

np.random.seed(0)
left = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': np.random.randn(4)})
right = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': np.random.randn(4)})


print(left)
print(right)
print(left.merge(right, on='key', how='inner'))
print(left.merge(right, on='key', how='left'))
print(left.merge(right, on='key', how='right'))
print(left.merge(right, on='key', how='outer'))