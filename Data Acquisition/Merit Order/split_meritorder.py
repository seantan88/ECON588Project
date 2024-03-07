# File Description: Split daily_merit_trim_asset.csv into csv files for each unique year and month 
# Author: Sean Tan 

import pandas as pd

# read the csv file into a dataframe
df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/daily_merit_trim_asset.csv")

# convert the date column to a datetime object
df1['begin_dateTime_mpt'] = pd.to_datetime(df1['begin_dateTime_mpt'])

# create a list of the unique years in the date column
years = df1['begin_dateTime_mpt'].dt.year.unique()

# create a list of the unique months in the date column
months = df1['begin_dateTime_mpt'].dt.month.unique()

# create a dictionary to store the dataframes
df_dict = {}

# iterate through the unique years
for year in years:
    # iterate through the unique months
    for month in months:
        # create a dataframe for each year and month
        df2 = df1[(df1['begin_dateTime_mpt'].dt.year == year) & (df1['begin_dateTime_mpt'].dt.month == month)]
        # add the dataframe to the dictionary
        df_dict[f'{year}_{month}'] = df2



# save each dataframe to a csv file
for key, value in df_dict.items():
    value = value[['begin_dateTime_mpt', 'asset_ID', 'block_price', 'offer_control']]
    value.to_csv(f'{key}.csv')





        

