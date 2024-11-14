import pandas as pd
import numpy as np

print(pd.date_range(start = '01-01-2023', end = '02-02-2023'))

data = {'col1': [1,2], 'col2': [3,4], 'col3': ['tom','jerry']}
df = pd.DataFrame(data=data)
print(df)
print(df.mean(numeric_only=True))

dates = pd.date_range("20200101", periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=["Cat1", "Cat2", "Cat3", "Cat4"])
print(df)
print(df.describe())