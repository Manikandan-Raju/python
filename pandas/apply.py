import pandas as pd

def calc_sum(x):
    return x.sum()

data = {
"x": [50, 40, 30],
"y": [300, 1112, 42]
}

df = pd.DataFrame(data)

print(df)
a = df['x'].sum()
print(a)
x = df.apply(calc_sum)
x = df.assign(l = lambda x: x.x + x.y)
print(x)