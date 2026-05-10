import pandas as pd
df=pd.read_csv("Hyd_rent_data.csv")
print(df)
print(df.isnull().sum())
df=df.dropna()
print(df.isnull().sum())

df=df[["Bhk", "Price", "Locality"]]
df.rename(columns={"Area": "Area_sqrt"}, inplace=True)
df.rename(columns={"Locality": "Location"}, inplace=True)
print(df.head(5))
print(df.columns)

df.to_csv("hyd_cleaned.csv", index=False)
print("saved successfully")
