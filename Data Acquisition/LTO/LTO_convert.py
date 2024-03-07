# File Description: (NOT WORKING AS INTENDED) Convert AESO_2024LTO.xlsx to csv files for each sheet
# Author: Sean Tan

import pandas as pd
import openpyxl as opx


df1 = pd.read_excel(r"C:\Users\seanh\Documents\GitHub\ECON588Project\AESO_2024LTO.xlsx")


#convert the first page of the excel file into a csv file
df1.to_csv('AESO_2024LTO.csv')

# open the excel file
wb = opx.load_workbook(r"C:\Users\seanh\Documents\GitHub\ECON588Project\AESO_2024LTO.xlsx")
# get the names of the sheets
sheet_names = wb.sheetnames
# iterate through the sheets and convert them to csv files
for sheet in sheet_names:
    df = pd.read_excel(r"C:\Users\seanh\Documents\GitHub\ECON588Project\AESO_2024LTO.xlsx", sheet_name = sheet)
    df.to_csv(f'{sheet}.csv')

# now, we have a csv file for each sheet in the excel file
# we can now use these csv files for future analysis


    