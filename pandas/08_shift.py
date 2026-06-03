import pandas as pd

# sample DataFrame with datetime index
date_rng = pd.date_range(start='2020-01-01', end='2020-01-03', freq='D')
data = {'Value': [10, 20, 30]}

df = pd.DataFrame(data, index=date_rng)

print(df)

# shift data by one day using freq argument
shifted_df = df.shift(freq='D')

print(shifted_df)