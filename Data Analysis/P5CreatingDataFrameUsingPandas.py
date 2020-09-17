import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df)

df1 = pd.DataFrame([[1,2,3,4], [5,6,7,8], [1,5,1,62], [432,635,13,73], [12,73,134,523]]
                   , columns=['A', 'B', 'C', 'D'])  #this will name the column as the list passed to it
# print(df1)

# ways to print our DataFrame
# print(df1.head(2))   #this will print the first two lists of the DataFrame

# print(df1.tail(2))    #this will print the last two lists of the DataFrame

# shape()
print(df1.shape)   #this will print the rows and column of hte DataFrame
# here it is printing 5 rows and 4 columns

# iloc() for accessing the elements of the DataFrame
print(df1.iloc[0:2, 1:3])