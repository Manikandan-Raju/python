import numpy as np
import pandas as pd

# Create a DataFrame with speed and distance values.
t = np.linspace(0, 1, 11)
s = np.random.randint(40, 60, 11)
d = np.random.randint(20, 40, 11)

df = pd.DataFrame(
    {"speed": s, "distance": d},
    index=t,
)
print("Original DataFrame:")
print(df)
print()

print("Filtered rows where speed < 50 and distance > 30:")
event = df[(df["speed"] < 50) & (df["distance"] > 30)]
print(event)

