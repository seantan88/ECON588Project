#Make the Marginal Cost Calculations CSV
#Author: Emily Deuchar

import pandas as pd
#Read it into a dataframe
Marginal_cost_df = pd.read_csv(r'~/OneDrive/Documents/GitHub/ECON588PROJECT/CSV data/Merit Order Data/Marginal_cost.csv')

#Create a variable for Fuel cost
Fuel_cost=Marginal_cost_df['Fuel_cost']
# Create a list of date ranges for each month
date_ranges = pd.date_range(start='2023-01-01', end='2023-12-31', freq='MS')

# Create a DataFrame to store the calculated values
calculation_df = pd.DataFrame(columns=['Date', 'Calculated Value'])

# Create an empty DataFrame to store the calculated values
calculation_df = pd.DataFrame(columns=['Date', 'Fuel Cost', 'Calculated Value'])

# Loop over each fuel cost
for i, fuel_cost in enumerate(Fuel_cost):
    # Extract the date range for the current month
    date_range = date_ranges[i]
    
    # Extract year and month from the date range
    year = date_range.year
    month = date_range.month
    
    # Perform the calculation for the current fuel cost
    calculated_value = (fuel_cost * 6.79) + 3.65 + 25
    
    # Append the calculated value for each day of the month
    month_dates = pd.date_range(start=date_range, end=date_range + pd.offsets.MonthEnd(), freq='D')
    
    # Create a DataFrame for the current fuel cost
    df = pd.DataFrame({
        'Date': month_dates,
        'Fuel Cost': [fuel_cost] * len(month_dates),
        'Calculated Value': [calculated_value] * len(month_dates)
    })
    
    # Concatenate the DataFrame to the main DataFrame
    calculation_df = pd.concat([calculation_df, df], axis=0)

# Reset the index
calculation_df.reset_index(drop=True, inplace=True)

# Save the result to a CSV file
calculation_df.to_csv('Marginal_cost_calculation.csv', index=False)