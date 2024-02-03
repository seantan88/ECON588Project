import json
import requests
import datetime
import time
import pandas as pd

#January 2019 - January 2020 data:
api_url = 'https://api.aeso.ca/report/v1.1/price/poolPrice?startDate=2023-01-01&endDate=2023-12-31'


jan = datetime.date(2023,1,1)
dec = datetime.date(2023,12,31)



query_params = {'startDate': jan, 'endDate': dec}
AESO_header = {'accept': 'application/json' , 'X-API-Key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJydmM2d2IiLCJpYXQiOjE3MDYwMjMyNzB9.zWQ2w5TnM9keQRNZwrTBAKRnQMKEMF4D5tnbLWV6WDQ'}

res = requests.get(api_url, query_params, headers = AESO_header)

data = json.loads(res.text)

print(data)



