import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

d= {'col1': [1,2], 'col2': [3,4], 'col3': ['tom','jerry']}
df = pd.DataFrame(data=d)
df.plot(kind="bar",x='col1',y='col2')
plt.show()

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()