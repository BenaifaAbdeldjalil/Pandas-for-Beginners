import pandas as pd 
import openpyxl

#read CSV
#df = pd.read_csv("dataset/world_population.csv", sep=",") 
#print(df[:2])

#index 
#make country as index
df = pd.read_csv("dataset/world_population.csv",index_col="Country", sep=",") 
print(df[:2])

#reset_index for reset
df.reset_index(inplace=True)

#or
##make CCA3 as index
df.set_index("CCA3",inplace=True)
print(df[:2])

#loc #value ex=ALB should be in the index column
print(df.loc["ALB"])

#iloc is the same thins but by index (integer) index location==>iloc
print(df.iloc[2])

#multipl index
#reset index
df.reset_index(inplace=True)
df.set_index(['Continent',"Country"],inplace=True)

#order index
df.sort_index(ascending=[True,False],inplace=True)
print(df[:10])
df.sort_index(ascending=[False,True],inplace=True)
print(df[:10])
df.sort_index(inplace=True)
print(df[:10])

print(df.loc['Africa','Algeria'])


#but 
print(df.iloc[1]) #Name: (Africa, Angola), dtype: objec
#because loc and iloc don't work in same logique 







