import pandas as pd

df= pd.read_excel("Dataset for Data Analytics.xlsx")


#Understanding the data
print(df.head())
df.info()


#Removing duplicates
print(f"Duplicates values count in the data {df.duplicated().sum()}")


#removing null values
print(f"Total null values present in the dataset along with the column name\n  {df.isnull().sum()}")
print(f"Total null values present in the dataset {df.isnull().sum().sum()}")
df["CouponCode"]=df["CouponCode"].fillna("No Coupon")
print(df.head())
print(f"Total null values present in the dataset after removing {df.isnull().sum().sum()}")


#Fix datatypes
print(df.dtypes)
df["Date"]=pd.to_datetime(df["Date"], errors="coerce")
wrong_date_format=df["Date"].isnull().sum() 
print(f"Total number of incorrect date format is {wrong_date_format}")

#standardization
text_cols=df.select_dtypes(include=["object"]).columns
num_cols=df.select_dtypes(include=["int64","float64"]).columns

for col in text_cols:
    df[col]=df[col].str.strip().str.title()

df["CouponCode"]=df["CouponCode"].str.upper()
df["UnitPrice"]=df["UnitPrice"].round(2)
df["TotalPrice"]=df["TotalPrice"].round(2)

print(df.head())

for cols in text_cols:
    if not df[cols].is_unique:
        print(df[cols].value_counts())


#Validate data logic
for col in num_cols:
    if (df[col]<0).any():
        print(f"Wrong numeric values enter in {col} columns")
    else:
        print(f"Correct numeric values enter in {col} columns")

#FINAL CHECK
print("\n----------FINAL CHECK----------")
print(f"Number of missing values after cleaning the data is {df.isnull().sum().sum()}")
print(f"Number of duplicates values after cleaning the data is {df.duplicated().sum()}")
print(f"Number of incorrect date format is {df['Date'].isnull().sum()}")
print(f"Number of duplicate ID is {df['OrderID'].duplicated().sum()}")
print(f"Data Information ")
df.info()


#Save the Cleaned file
choice=input("\nEnter 'Y' for saving the cleaned excel file : ")
if choice.strip().upper()=="Y":
    df.to_excel("CleanedData.xlsx", index=False)
    print("CleanedData.xlsx file successfully downloaded in the current directory. ")