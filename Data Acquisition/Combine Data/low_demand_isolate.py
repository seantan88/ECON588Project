# File Description: Isolate low demand hours from CSD_Merit_2023.csv, and split into monthly csv files, as well as monthly csv files for each asset
# Author: Sean Tan

import pandas as pd


df = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Combined Data/CSD_Merit_2023.csv")

# trim the dataframe to only include hours between 11pm and 7am, each date called 'begin_dateTime_mpt' row is formatted as 'yyyy-mm-dd hh:mm:ss'
df = df[(df['begin_dateTime_mpt'].str[11:13] >= '23') | (df['begin_dateTime_mpt'].str[11:13] <= '07')]



#split this data into monthly csv files
df['begin_dateTime_mpt'] = pd.to_datetime(df['begin_dateTime_mpt'])
years = df['begin_dateTime_mpt'].dt.year.unique()
months = df['begin_dateTime_mpt'].dt.month.unique()
df_dict = {}
for year in years:
    for month in months:
        df2 = df[(df['begin_dateTime_mpt'].dt.year == year) & (df['begin_dateTime_mpt'].dt.month == month)]
        df_dict[f'{year}_{month}'] = df2

for key, value in df_dict.items():
    value = value[['begin_dateTime_mpt', 'block_price', 'System Capability', 'asset_ID']]
    value.to_csv(f'low_demand_isolate_{key}.csv')

#split the data frames further into individual asset csv files
for key, value in df_dict.items():
    assets = value['asset_ID'].unique()
    for asset in assets:
        df3 = value[(value['asset_ID'] == asset)]
        df3 = df3[['begin_dateTime_mpt', 'block_price', 'System Capability', 'asset_ID']]
        df3.to_csv(f'low_demand_isolate_{key}_{asset}.csv')



