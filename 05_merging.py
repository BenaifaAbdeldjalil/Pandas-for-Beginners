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

#cross
print("##############df7#################")
df8 = df1.merge(df2,how="cross")
print(df8)

# --------------------------Join---------------------------
print("--------------------------Join---------------------------")
# dfj1=df1.join(df2) #ValueError: columns overlap but no suffix specified: Index(['FellowshipID', 'FirstName'], dtype='str')

dfj1=df1.join(df2,on="FellowshipID",how="outer",lsuffix="_l",rsuffix="_r")
print(dfj1)
dfj2=df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'),lsuffix="_l")
print(dfj2)
#   OR
dfj3=df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'),lsuffix="_l",on="FellowshipID")
print(dfj3)


# --------------------------concat---------------------------
print("--------------------------concat---------------------------")
#option 1 
df_concat=pd.concat([df1,df2]) #===df_concat1=pd.concat([df1,df2],join='outer')
print(df_concat)

#option 2
df_concat1=pd.concat([df1,df2],join='inner') #only inner or outer
print(df_concat1)

df_concat2=pd.concat([df1,df2],join='outer') #only inner or outer
print(df_concat2)

df_concat3=pd.concat([df1,df2],join='outer',axis=1) #only inner or outer
print(df_concat3)

df_concat4=pd.concat([df1,df2],join='outer',axis=0) #only inner or outer
print(df_concat4)







