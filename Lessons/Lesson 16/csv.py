import pandas as pd
import matplotlib.pyplot as plt

f = open('data.csv', 'a')
f.write('tom')
df = pd.read_csv('data.csv')

df.plot()
print(df.describe())
plt.show()
f.close()