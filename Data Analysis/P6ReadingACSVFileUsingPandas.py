import pandas as pd

df = pd.read_csv('Data.csv')    #this will read the csv file
print(df)

print(df['Date'].dtype)   #this will print the datatype