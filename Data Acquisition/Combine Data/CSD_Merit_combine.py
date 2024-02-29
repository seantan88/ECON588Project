import pandas as pd


df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/CSD Data/CSD Generation (Hourly) - 2023-01 to 2023-06.csv")
df2 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/Monthly Data/daily_merit_first6mos.csv")

# rename Asset Short Name to 'asset_ID' in df1
df1.rename(columns = {'Asset Short Name': 'asset_ID'}, inplace = True)
# rename Date (MPT) to 'begin_dateTime_mpt' in df1
df1.rename(columns = {'Date (MPT)': 'begin_dateTime_mpt'}, inplace = True)
# drop unnecessary columns in df1
df1 = df1[['begin_dateTime_mpt', 'asset_ID', 'System Capability']]
# merge the two dataframes on the 'asset_ID' and 'begin_dateTime_mpt' columns
df3 = pd.merge(df1, df2, on = ['asset_ID', 'begin_dateTime_mpt'], how = 'inner')





# drop unnecessary columns
df3 = df3[['begin_dateTime_mpt','block_price', 'System Capability', 'asset_ID']]
# drop any rows with NaN values
df3 = df3.dropna()
# save the combined dataframe to a csv file
df3.to_csv('CSD_Merit_2023.csv')