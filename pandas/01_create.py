# Pandas does not have pd.zeros / pd.ones / pd.random directly.
# Use NumPy arrays and wrap them in pandas if needed.
# Example:
# import pandas as pd
# df = pd.DataFrame(np.zeros((3, 4)))
# df = pd.DataFrame(np.ones((2, 5)))
# s = pd.Series(np.random.random(6))