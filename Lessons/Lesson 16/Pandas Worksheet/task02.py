import pandas as pd
df = pd.DataFrame({"A":[4, 5, 2, 6],
"B":[11, 2, 5, 8],
"C":[1, 8, 66, 4]})
#print(df) # prints all the data on the table
#print(df[2:8])
print(df.iloc[ : -4 , : ])
