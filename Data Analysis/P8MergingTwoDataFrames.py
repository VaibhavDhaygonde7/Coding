import pandas as pd

df1 = pd.DataFrame([[11,7,312], [22,12,35], [63,3,92]], columns=['A', 'B', 'C'])
df2 = pd.DataFrame([[1,2,3], [2,7,3], [6,3,9]], columns=['X', 'Y', 'Z'])

df3 = pd.merge(df1, df2, right_on='Y', left_on='B')
print(df3)