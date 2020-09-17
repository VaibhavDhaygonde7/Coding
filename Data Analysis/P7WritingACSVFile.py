import pandas as pd

df1 = pd.DataFrame([[1,2,3,4], [5,6,7,8], [1,5,1,62], [432,635,13,73],
                    [12,73,134,523]],
                   columns=['A', 'B', 'C', 'D'])

df1.to_csv('Export.csv', index=False)  #this will create a new csv file and will have the content
                          #which is written here

#by writing index = False we remove the extra column of the numbers in the csv file
                          