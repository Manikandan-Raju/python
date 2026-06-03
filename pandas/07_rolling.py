import pandas as pd

# sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})
print(df)

# rolling with different closed values
print("Closed on right (default):")
print(df.rolling(window=2, closed='right').sum()) 

print("\nClosed on left:")
print(df.rolling(window=2, closed='left').sum())

print("\nClosed on both:")
print(df.rolling(window=2, closed='both').sum())

print("\nClosed on neither:")
print(df.rolling(window=2, closed='neither').sum())