import pandas as pd 
import openpyxl

#read CSV
df = pd.read_csv("dataset/Flavors.csv", sep=",") 
#print(df[:2])

#groupby
df_grouby = df.groupby('Base Flavor')

#groupby methode
df_grouby.sum()
df_grouby.mean(numeric_only=True)
df_grouby.count()
df_grouby = df.groupby('Base Flavor').max()
df_grouby = df.groupby('Base Flavor').min()
df.groupby('Base Flavor').agg({'Flavor Rating':['mean','max','min','count']})


df_grouby = df.groupby(['Base Flavor','Liked']).mean(numeric_only=True)

#OR
df1=df.groupby('Base Flavor').mean(numeric_only=True)
print(df_grouby.mean(numeric_only=True))
print(df.groupby('Base Flavor').min())
print(df.groupby('Base Flavor').max())
print(df.groupby('Base Flavor').agg({'Flavor Rating':['mean','max','min','count']}))
print(df.groupby(['Base Flavor','Liked']).mean(numeric_only=True))
print(df.groupby(['Base Flavor','Liked']).max())

#describe
print(df.groupby(['Base Flavor','Liked']).describe().columns)

#











