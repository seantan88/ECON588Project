
import pandas as pd



df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/CSD Data/CSD Generation (Hourly) - 2023-01 to 2023-06.csv")
df2 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/CSD Data/CSD Generation (Hourly) - 2023-07 to 2023-12.csv")

# combine the two dataframes
df3 = pd.concat([df1, df2])

# drop unnecessary columns
df3 = df3[['Date (MPT)', 'Asset Short Name', 'Sub Fuel Type', 'Planning Area', 'Region']]
df3 = df3[df3['Sub Fuel Type'] == 'COMBINED_CYCLE']

# save the combined dataframe to a csv file
df3.to_csv('CSD_Generation_2023.csv')





