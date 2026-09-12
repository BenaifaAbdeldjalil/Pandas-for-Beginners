import pandas as pd 
import openpyxl

#read CSV
df1 = pd.read_excel("dataset/Customer Call List.xlsx") 

print(df1) #[21 rows x 8 columns]

#duplicate data
df=df1.drop_duplicates()
print(df) #[20 rows x 8 columns]
#print(df2[:2])

#drop unusful columns
print(df.columns) #['CustomerID', 'First_Name', 'Last_Name', 'Phone_Number', 'Address','Paying Customer', 'Do_Not_Contact', 'Not_Useful_Column']
n_usful=["Not_Useful_Column","Do_Not_Contact"]
df.drop(columns=n_usful,inplace=True)
print(df.columns) #['CustomerID', 'First_Name', 'Last_Name', 'Phone_Number', 'Address','Paying Customer']

#cleaning data
#remove caracteres left and right
#df['Last_Name']=df['Last_Name'].str.strip()
#df['Last_Name']=df['Last_Name'].astype(str).str.strip("...")
#df['Last_Name']=df['Last_Name'].astype(str).str.strip("/")
#df['Last_Name']=df['Last_Name'].astype(str).str.strip("_")

#OR 
df['Last_Name']=df['Last_Name'].str.strip("123./_")
print(df)

#phone number
df['Phone_Number']=df['Phone_Number'].str.replace('[^a-zA-Z-0-9]','')
print(df['Phone_Number'])
df['Phone_Number']=df['Phone_Number'].apply(lambda x: x[0-3]+'-'+[3-5]+'-'+[6-10])
print(df['Phone_Number'])













