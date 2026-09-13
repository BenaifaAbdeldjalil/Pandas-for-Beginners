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
df['Phone_Number']=df['Phone_Number'].str.replace(r'[^a-zA-Z0-9]',"",regex=True)
print(df['Phone_Number'])

# OR
#df['Phone_Number'] = df['Phone_Number'].str.replace(r'\D', '', regex=True)

#remouve NaN and Na
print("------------------")
df['Phone_Number']=df['Phone_Number'].fillna("").replace("Na","")
print(df['Phone_Number'])

# make phone number as xxx-xxx-xxx
df['Phone_Number']=df['Phone_Number'].apply(lambda x: x[:3]+"-"+x[3-5]+"-"+x[6-10]  if isinstance(x, str) and len(x) >= 10
    else x)
print(df['Phone_Number'])













