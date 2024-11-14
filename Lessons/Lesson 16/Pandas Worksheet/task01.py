#prints out all the data in a series
import pandas as pd
s1=pd.Series([1,2,2,7,'Sachin',77.5])
print(s1.head())
print(s1.head(3))