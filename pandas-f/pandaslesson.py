import pandas as pd
s=pd.Series([9, 3,32 , 4, 5])
# print(s)
print(s[0])
print(s[1:4])
s.index=['a','b','c','d','e']
print(s['e'])