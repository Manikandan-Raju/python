# 10_pivot_table.py
# Demonstrates pivot_table and reshaping with pandas.

import pandas as pd
import numpy as np

np.random.seed(2)
df = pd.DataFrame({
    'region': ['East', 'West', 'East', 'West', 'East', 'West'],
    'product': ['A', 'A', 'B', 'B', 'A', 'B'],
    'sales': np.random.randint(10, 50, size=6),
})

print('DataFrame:')
print(df)
print()

print('Pivot table by region and product:')
print(pd.pivot_table(df, index='region', columns='product', values='sales', aggfunc='sum'))
