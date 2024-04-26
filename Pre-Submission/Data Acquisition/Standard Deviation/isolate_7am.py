# File description: Isolate the 7 am data from the combined CSD and Merit Order data for the first 6 months of 2023
# Author: Sean Tan

import pandas as pd
df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Combined Data/CSD_Merit_2023.csv")

# this dataframe contains the combined CSD and Merit Order data for the first 6 months of 2023. The columns are: begin_dateTime_mpt, block_price, System Capability, and asset_ID. Trim this dataframe to only include 7 am data, indicated by the 'begin_dateTime_mpt' column having 'YYYY-MM-DD 07:00:00' as the value
df1 = df1[(df1['begin_dateTime_mpt'].str[11:19] == '07:00:00')]
print(df1)
# save the dataframe to a csv file
#df1.to_csv('isolate_7am.csv')

# further split the dataframes into individual asset csv files
assets = df1['asset_ID'].unique()
for asset in assets:
    df2 = df1[(df1['asset_ID'] == asset)]
    # drop the first columns which is unnecessary
    df2 = df2[['begin_dateTime_mpt', 'block_price', 'System Capability', 'asset_ID']]
    df2.to_csv(f'isolate_7am_{asset}.csv')



















