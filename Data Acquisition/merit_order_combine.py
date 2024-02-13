# import necessary packages
import json
import requests
import datetime
import time
import pandas as pd

# initialize dates for length of data to be requested
jan = datetime.date(2023,1,1)
jun = datetime.date(2023,6,1).strftime('%Y-%m-%d')
dec = datetime.date(2023,12,31).strftime('%Y-%m-%d')


master_df = pd.DataFrame()

for i in range(2):
    date = jan.strftime('%Y-%m-%d')

    # initialize api url with changeable dates
    api_url = f'https://api.aeso.ca/report/v1/meritOrder/energy?startDate={jan}'

    # initialize requests header, including valid API key
    AESO_header = {'accept': 'application/json' , 'X-API-Key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJydmM2d2IiLCJpYXQiOjE3MDYwMjMyNzB9.zWQ2w5TnM9keQRNZwrTBAKRnQMKEMF4D5tnbLWV6WDQ'}

    # request data from AESO API, load the JSON
    res = requests.get(api_url, headers = AESO_header)
    data = json.loads(res.text)

    # normalize the JSON data into flat table
    df1 = pd.json_normalize(data)
    #print(df1.info())

    # get list of dictionaries from df
    df1_list = df1.loc[0, 'return.data']

    # convert list of dictionaries into readable and clean dataframe ready for usage
    df2 = pd.DataFrame(df1_list)

    master_df = pd.concat([master_df,df2], axis=0, ignore_index =True)

    # print first 5 rows of cleaned dataframe to verify correct format
    jan = jan + datetime.timedelta(days=1)






daily_master_df = pd.DataFrame()

for index, row in master_df.iterrows():
    if 'energy_blocks' in row and isinstance(row['energy_blocks'], list):
        df_temp = pd.DataFrame(row['energy_blocks'])
        # Attach the timestamp from df2 to df_temp
        df_temp['begin_dateTime_mpt'] = row['begin_dateTime_mpt']  
        daily_master_df = pd.concat([daily_master_df, df_temp], axis=0, ignore_index=True)
    

daily_master_df.to_csv('daily_merit.csv')





