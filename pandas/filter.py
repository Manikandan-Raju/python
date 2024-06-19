import numpy as np
import pandas as pd

t = np.linspace(0,1,11)

s = np.random.randint(40,60,11)
d = np.random.randint(20,40,11)

df = pd.DataFrame(zip(s,d),index=t,columns=['speed','distance'])
print(df)

event = df[(df['speed'] < 50) & (df['distance'] > 30)]

print(event)

