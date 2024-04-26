import pandas as pd

# read the csv file into a dataframe
df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/CSD Data/CSD Generation (Hourly) - 2023-01 to 2023-06.csv")

# remove all columns except for the following: Asset Short Name, Fuel Type, Sub Fuel Type
df1 = df1[['Asset Short Name', 'Fuel Type', 'Sub Fuel Type']]
# remove all rows with NaN values
df1 = df1.dropna()

# remove duplicates
df1 = df1.drop_duplicates()

# save the dataframe to a csv file

df1.to_csv('generator_type.csv')