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


#OR
df1=df.groupby('Base Flavor').mean(numeric_only=True)
print(df_grouby.mean(numeric_only=True))
print(df.groupby('Base Flavor').min())
print(df.groupby('Base Flavor').max())

