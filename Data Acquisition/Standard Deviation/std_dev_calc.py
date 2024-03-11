import pandas as pd

df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_CAL1.csv")
df2 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_CMH1.csv")
df3 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_EC01.csv")
df4 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_EGC1.csv")
df5 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_FNG1.csv")
df6 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_NX01.csv")

df_list = [df1, df2, df3, df4, df5, df6]
generator_list = ['CAL1', 'CMH1', 'EC01', 'EGC1', 'FNG1', 'NX01']
# df1 - df6 contain the first 6 months of 2023 7 am data for the 6 generating assets, calculate the standard deviation and average for the block_price column each month. Make a new csv file with the months in the rows and columns that include asset_ID, average, and standard deviation
df_dict = {}

for i in range(len(df_list)):
    df_dict[f'{generator_list[i]}'] = df_list[i]


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
    df_dict[f'{key}'] = df_dict2

# calculate the average block price for each asset for each month, and amalgamate the data into a single csv file
df_dict3 = {}
for key, value in df_dict.items():
    df_dict4 = {}
    for key2, value2 in value.items():
        df4 = value2['block_price'].mean()
        df_dict4[f'{key2}'] = df4
    df_dict3[f'{key}'] = df_dict4
df5 = pd.DataFrame(df_dict3)
df5.to_csv('asset_monthly_average.csv')

# calculate the standard deviation for each asset for each month, and amalgamate the data into a single csv file
df_dict6 = {}
for key, value in df_dict.items():
    df_dict7 = {}
    for key2, value2 in value.items():
        df7 = value2['block_price'].std()
        df_dict7[f'{key2}'] = df7
    df_dict6[f'{key}'] = df_dict7
df8 = pd.DataFrame(df_dict6)
df8.to_csv('asset_monthly_std_dev.csv')
    



    




