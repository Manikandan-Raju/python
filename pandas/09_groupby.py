# 09_groupby.py
# Demonstrates groupby aggregation and grouping operations in pandas.

import pandas as pd
import numpy as np

np.random.seed(1)

df = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B', 'C', 'C'],
    'score': np.random.randint(1, 10, size=6),
    'age': [23, 24, 22, 25, 24, 23],
})
print('DataFrame:')
print(df)
print()

print('Group by team, sum of score:')
print(df.groupby('team')['score'].sum())
print()

print('Group by team, aggregated statistics:')
print(df.groupby('team').agg({'score': ['mean', 'max'], 'age': 'min'}))
