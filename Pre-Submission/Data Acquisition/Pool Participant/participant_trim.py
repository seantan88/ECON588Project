
import pandas as pd

df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/CSD Data/CSD_Generation_2023.csv")

#get a list of all unique asset names from the 'asset short name' column in df1
asset_list = df1['Asset Short Name'].unique()


df2 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/daily_merit_trim.csv")

#use this list to delete any rows in df2 that do not have an asset name in this list
df2 = df2[df2['asset_ID'].isin(asset_list)]

df2.to_csv('daily_merit_trim_asset.csv')