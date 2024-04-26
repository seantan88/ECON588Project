# File Description: Monthly aggregation of electricity generation asset data
# Author: Sean Tan

import pandas as pd

df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Combined Data/CSD_Merit_2023.csv")

#get a list of all unique asset names from the 'asset_ID' column in df1
asset_list = df1['asset_ID'].unique()

#use the list of unique asset names to get individual dataframes for each asset in df1
df_dict = {}

for asset in asset_list:
    df2 = df1[df1['asset_ID'] == asset]
    df_dict[f'{asset}'] = df2
    df_dict[f'{asset}'] = df_dict[f'{asset}'][['begin_dateTime_mpt', 'block_price', 'System Capability', 'asset_ID']]

#for key, value in df_dict.items():
    #value.to_csv(f'{key}.csv')

# split the asset specific dataframes further into monthly csv files, with asset and month specified in the file name, 'begin_dateTime_mpt' row is formatted as 'yyyy-mm-dd hh:mm:ss'
for key, value in df_dict.items():
    # convert the date column to a datetime object
    value['begin_dateTime_mpt'] = pd.to_datetime(value['begin_dateTime_mpt'])
    years = value['begin_dateTime_mpt'].dt.year.unique()
    months = value['begin_dateTime_mpt'].dt.month.unique()
    df_dict2 = {}
    for year in years:
        for month in months:
            df3 = value[(value['begin_dateTime_mpt'].dt.year == year) & (value['begin_dateTime_mpt'].dt.month == month)]
            df_dict2[f'{year}_{month}'] = df3
    for key2, value2 in df_dict2.items():
        value2.to_csv(f'{key}_{key2}.csv')

#calculate the average block price for each asset for each month, and amalgamate the data into a single csv file
df_dict3 = {}
for key, value in df_dict.items():
    df4 = value.groupby(value['begin_dateTime_mpt'].dt.strftime('%Y-%m'))['block_price'].mean()
    df_dict3[f'{key}'] = df4
df5 = pd.DataFrame(df_dict3)
df5.to_csv('asset_monthly_average.csv')

    















