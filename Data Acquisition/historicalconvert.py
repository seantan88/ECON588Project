
import pandas as pd


df1 = pd.read_csv(r"C:\Users\seanh\Documents\GitHub\ECON588Project\CSV data\CSD Generation (Hourly) - 2023-01 to 2023-06.csv")
df2 = pd.read_csv(r"C:\Users\seanh\Documents\GitHub\ECON588Project\CSV data\CSD Generation (Hourly) - 2023-07 to 2023-12.csv")

print(df1.head())
print(df2.head())
