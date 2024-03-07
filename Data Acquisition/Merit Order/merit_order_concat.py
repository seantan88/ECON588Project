# File Description: Combine Merit Order data for the first 6 months of 2023, refine data to only include the following columns: begin_dateTime_mpt, asset_ID, block_price, and offer_control, and save to a csv file
# Author: Sean Tan

import pandas as pd

# read the csv files into dataframes
df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/Monthly Data/2023_1.csv")
df2 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/Monthly Data/2023_2.csv")
df3 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/Monthly Data/2023_3.csv")
df4 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/Monthly Data/2023_4.csv")
df5 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/Monthly Data/2023_5.csv")
df6 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/Monthly Data/2023_6.csv")

# combine the dataframes
df7 = pd.concat([df1, df2, df3, df4, df5, df6])

# drop unnecessary columns
df7 = df7[['begin_dateTime_mpt', 'asset_ID', 'block_price', 'offer_control']]

# convert the dataframe to csv file
df7.to_csv('daily_merit_first6mos.csv')
