import pandas as pd 
import openpyxl

#read CSV
df1 = pd.read_csv("dataset/LOTR.csv", sep=",") 
df2 = pd.read_csv("dataset/LOTR 2.csv", sep=",") 
print(df1[:2])
print(df2[:2])


#merge
df3 = df1.merge(df2)
print(df3)