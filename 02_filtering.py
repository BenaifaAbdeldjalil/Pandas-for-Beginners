import pandas as pd 
import openpyxl

#read CSV
df = pd.read_csv("dataset/world_population.csv") #SyntaxError: Non-UTF-8 code starting with '\xff'

filtre = df["Rank"]>50
#print(df[filtre]) #[184 rows x 17 columns]

#or
print(df[df["Rank"]>50]) #[184 rows x 17 columns]

