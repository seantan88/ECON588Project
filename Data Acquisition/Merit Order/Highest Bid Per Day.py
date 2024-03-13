# File discription: Create a variable that has only the greatest bids from each **day**
#Author: Emily Deuchar
import pandas as pd

# Read the csv file into a dataframe
bids_df = pd.read_csv(r"~/OneDrive/Documents/GitHub/ECON588PROJECT/CSV data/Merit Order Data/daily_merit_trim_asset.csv")

# Convert the date column to a datetime object
bids_df['begin_dateTime_mpt'] = pd.to_datetime(bids_df['begin_dateTime_mpt'])

# Create a new column 'date' to store only the date part of 'begin_dateTime_mpt'
bids_df['date'] = bids_df['begin_dateTime_mpt'].dt.date

# Group by date and asset ID, and find the row with the highest block price for each asset ID on each day
highest_block_prices_df = bids_df.loc[bids_df.groupby(['date', 'asset_ID'])['block_price'].idxmax()]

# Save the result to a CSV file
highest_block_prices_df.to_csv('highest_block_prices_per_day.csv', index=False)