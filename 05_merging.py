import pandas as pd 
import openpyxl

#read CSV
df1 = pd.read_csv("dataset/LOTR.csv", sep=",") 
df2 = pd.read_csv("dataset/LOTR 2.csv", sep=",") 
#print(df1[:2])
#print(df2[:2])


#merge inner
#df3 = left.merge(right)
#merge default == inner join
df3 = df1.merge(df2)
print(df3)

#OR 
df4 = df1.merge(df2,how="inner",on=["FellowshipID","FirstName"])
print(df4)
#or
print("##############df4#################")
df4 = df1.merge(df2,how="inner")
print(df4)

#left
print("##############df5#################")
df5 = df1.merge(df2,how='left')
print(df5)


#right
print("##############df6#################")
df6 = df1.merge(df2,how="right")
print(df6)


#outer
print("##############df7#################")
df7 = df1.merge(df2,how="outer")
print(df7)




