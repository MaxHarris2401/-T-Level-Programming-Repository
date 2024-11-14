import pandas as pd

data = {'name': ['Sanjeev','Keshav','Rahul'], 'age': [37,42,38], 'designation': ['manager','clerk','accountant']}
df = pd.DataFrame(data=data)
sdf = df.sort_values(by="age", ascending=True)
print(sdf)
ndf = df.sort_values(by="name", ascending=False)
print(ndf)