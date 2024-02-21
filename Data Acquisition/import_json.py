# Authors: Sean Tan, Emily Deuchar
# Description: AESO API call for pool price, convert JSON to clean and readable dataframe, convert cleaned dataframe to csv for further use

## TODO & NOTE ##
# - user input for date and api calls?
# - system marginal price and merit order have some issues regarding request restrictions
# - procedural vs functions?

# import necessary packages
import json
import requests
import datetime
import time
import pandas as pd

# initialize dates for length of data to be requested
jan = datetime.date(2023,1,1).strftime('%Y-%m-%d')
jun = datetime.date(2023,6,1).strftime('%Y-%m-%d')
dec = datetime.date(2023,12,31).strftime('%Y-%m-%d')

# initialize api url with changeable dates
api_url = f'https://api.aeso.ca/report/v1/poolparticipantlist'

# initialize requests header, including valid API key
AESO_header = {'accept': 'application/json' , 'X-API-Key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJydmM2d2IiLCJpYXQiOjE3MDYwMjMyNzB9.zWQ2w5TnM9keQRNZwrTBAKRnQMKEMF4D5tnbLWV6WDQ'}

# request data from AESO API, load the JSON
res = requests.get(api_url, headers = AESO_header)
data = json.loads(res.text)

# normalize the JSON data into flat table
df1 = pd.json_normalize(data)
#print(df1.head())

# get list of dictionaries from df
df1_list = df1.loc[0, 'return']

# convert list of dictionaries into readable and clean dataframe ready for usage
df2 = pd.DataFrame(df1_list)

#pool_price_df = pool_price_df.drop(['begin_datetime_utc'], axis=1)


# print first 5 rows of cleaned dataframe to verify correct format

print(df2.info())
df2.to_csv("pool_participant.csv")



