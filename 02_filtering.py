import pandas as pd 
import openpyxl

#read CSV
df = pd.read_csv("dataset/world_population.csv") #SyntaxError: Non-UTF-8 code starting with '\xff'

filtre = df["Rank"]>50
#print(df[filtre]) #[184 rows x 17 columns]

#or
print(df[df["Rank"]>50]) #[184 rows x 17 columns]


print(df[df["Rank"]<=50]) 
print(df[:5])

# isin filtering
country=["Algeria","Yemen"]
df_c= df["Country"].isin(country)
print(df[df_c])

# or 
df_contain= df["Country"].str.contains("Algeria")
print(df[df_contain])
df["s"] = df["Rank"].astype(str).str[0:1]


#filter column
df2=df.set_index("Country")
print(df2[:2].filter(items=["CCA3","Capital"],axis=1))

# or
filte= ["CCA3","Capital"]
print(df2[:2].filter(items=filte,axis=1))

#filter row
print(df2.filter(items=["Algeria"],axis=0))


#filter row
print(df2.filter(like="Afg",axis=0))

#loc
print(df2.loc["Algeria"])


#Iloc
print(df2.iloc[10])

#Orderby
print(df[df["Rank"]>50].sort_values(by='Rank',ascending=True))
print(df[df["Rank"]>50].sort_values(by=['Rank',"Country"],ascending=True))
print(df[df["Rank"]>50].sort_values(by=['Rank',"CCA3"],ascending=[False,True]))

