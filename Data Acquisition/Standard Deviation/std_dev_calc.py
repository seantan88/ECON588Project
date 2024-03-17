import pandas as pd

df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_CAL1.csv")
df2 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_CMH1.csv")
df3 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_EC01.csv")
df4 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_EGC1.csv")
df5 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_FNG1.csv")
df6 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Standard Deviation/7am/isolate_7am_NX01.csv")

df_list = [df1, df2, df3, df4, df5, df6]
generator_list = ['CAL1', 'CMH1', 'EC01', 'EGC1', 'FNG1', 'NX01']
# calculate the average block price and standard deviation of block price for each asset for each month, and amalgamate the data into a single csv file
df_dict = {}

for i in range(len(df_list)):
    df_dict[f'{generator_list[i]}'] = df_list[i]

# split the asset specific dataframes further into monthly dataframes
for key, value in df_dict.items():
    # convert the date column to a datetime object
    value['begin_dateTime_mpt'] = pd.to_datetime(value['begin_dateTime_mpt'])
    years = value['begin_dateTime_mpt'].dt.year.unique()
    months = value['begin_dateTime_mpt'].dt.month.unique()
    df_dict2 = {}
    # iterate through the unique years
    for year in years:
        # iterate through the unique months
        for month in months:
            # create a dataframe for each year and month
            df3 = value[(value['begin_dateTime_mpt'].dt.year == year) & (value['begin_dateTime_mpt'].dt.month == month)]
            # add the dataframe to the dictionary
            df_dict2[f'{year}_{month}'] = df3
    # add the dictionary to the main dictionary        
    df_dict[f'{key}'] = df_dict2

# calculate the average block price for each asset for each month, and amalgamate the data into a single csv file
# create a dictionary to store the average block price for each asset
df_dict3 = {}
# iterate through the main dictionary
for key, value in df_dict.items():
    # create a dictionary to store the average block price for each month
    df_dict4 = {}
    # iterate through the dictionary within the main dictionary
    for key2, value2 in value.items():
        # calculate the average block price for each month
        df4 = value2['block_price'].mean()
        # add the average block price to the dictionary
        df_dict4[f'{key2}'] = df4
    # add the dictionary to the main dictionary
    df_dict3[f'{key}'] = df_dict4 
# save the main dictionary to a csv file      
df5 = pd.DataFrame(df_dict3)
# save the main dictionary to a csv file
df5.to_csv('asset_monthly_average.csv')

# calculate the standard deviation for each asset for each month, and amalgamate the data into a single csv file
# create a dictionary to store the standard deviation for each asset
df_dict6 = {}
# iterate through the main dictionary
for key, value in df_dict.items():
    df_dict7 = {}
    # iterate through the dictionary within the main dictionary
    for key2, value2 in value.items():
        # calculate the standard deviation for each month
        df7 = value2['block_price'].std()
        # add the standard deviation to the dictionary
        df_dict7[f'{key2}'] = df7
        
    df_dict6[f'{key}'] = df_dict7
# save the main dictionary to a csv file    
df8 = pd.DataFrame(df_dict6)
# save the main dictionary to a csv file
df8.to_csv('asset_monthly_std_dev.csv')
    



    




