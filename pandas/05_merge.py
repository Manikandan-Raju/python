import numpy as np
import pandas as pd

np.random.seed(0)
left = pd.DataFrame(
    {
        "key": ["A", "B", "C", "D"],
        "value_left": np.random.randn(4),
    }
)
right = pd.DataFrame(
    {
        "key": ["B", "D", "E", "F"],
        "value_right": np.random.randn(4),
    }
)

print("Left DataFrame:")
print(left)
print()
print("Right DataFrame:")
print(right)
print()

print("Inner merge (only matching keys):")
print(left.merge(right, on="key", how="inner"))
print()

print("Left merge (all rows from left):")
print(left.merge(right, on="key", how="left"))
print()

print("Right merge (all rows from right):")
print(left.merge(right, on="key", how="right"))
print()

print("Outer merge (all rows from both):")
print(left.merge(right, on="key", how="outer"))
