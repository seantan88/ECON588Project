import pandas as pd
import numpy as np




df1 = pd.read_csv(r"C:\Users\seanh\Documents\GitHub\ECON588Project\CSV data\Merit Order Data\daily_merit.csv")

#remove every column except for the following: ID, block_number, block_price, and offer_control
df1 = df1[['begin_dateTime_mpt','asset_ID', 'block_number', 'block_price', 'offer_control']]

print(df1['asset_ID'].unique())

#df1.to_csv('daily_merit_trim.csv')
