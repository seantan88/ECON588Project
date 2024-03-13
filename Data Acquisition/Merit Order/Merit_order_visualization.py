#Create a merit order of highest bids at each hour:
#Author: Emily Deuchar
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df1 = pd.read_csv(r"~/OneDrive/Documents/GitHub/ECON588PROJECT/CSV data/Merit Order Data/daily_merit_trim_asset.csv")

# Convert the date column to a datetime object
df1['begin_dateTime_mpt'] = pd.to_datetime(df1['begin_dateTime_mpt'])

# Create a list of the unique years in the date column
years = df1['begin_dateTime_mpt'].dt.year.unique()

# Create a list of the unique months in the date column
months = df1['begin_dateTime_mpt'].dt.month.unique()

#Create a list of the unique days in each month column
days=df1['begin_datetime_mpt'].dt.day.unique()

#Create a list of the uniwue hours in each date column
hours = df1['begin_dateTime_mpt'].dt.hour.unique()

# Iterate through the unique years
for year in years:
    # Iterate through the unique months
    for month in months:
        #Iterate through the unique days
        for day in days:
            for hour in hours:
                # Create a DataFrame for each year and month
                df2 = df1[(df1['begin_dateTime_mpt'].dt.year == year) & (df1['begin_dateTime_mpt'].dt.month == month)&(df1['begin_datetime_mpt'].dt.day == day)&(df1['begin_datetime_mpt'].dt.hour == hour)]
        
                # Sort the DataFrame by asset ID
                df2 = df2.sort_values(by='asset_ID')
        
                # Visualize the data (scatter plot with markers)
                plt.figure(figsize=(12, 6))
                for asset_id in df2['asset_ID'].unique():
                    asset_data = df2[df2['asset_ID'] == asset_id]
                    plt.scatter(asset_data['begin_dateTime_mpt'], asset_data['block_price'], label=asset_id)
        
                plt.title(f'Merit Order of Power Plants')
                plt.xlabel('Date')
                plt.ylabel('Pool Price ($/MWh)')
                plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
                plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
                plt.tight_layout()
                plt.show()
#Marginal cost calculation: 
        
def calculate_marginal_cost_CAL1(electricity_output, fuel_cost_per_unit, variable_om_cost_per_unit, heat_rate, carbon_tax_rate):
    marginal_cost = (fuel_cost_per_unit / heat_rate) + variable_om_cost_per_unit + (carbon_tax_rate * heat_rate)

    total_cost = electricity_output * marginal_cost

    return total_cost

# Example data (replace these with actual values)
electricity_output = 330  # in MWh
fuel_cost_per_unit = 6.55   # in $/MMBtu or any unit of energy
variable_om_cost_per_unit = 3.6  # in $/MWh
heat_rate = 6435678  # in MMBtu/MWh
carbon_tax_rate = 65  # in $/ton of CO2

# Calculate marginal cost
marginal_cost = calculate_marginal_cost(electricity_output, fuel_cost_per_unit, variable_om_cost_per_unit, heat_rate, carbon_tax_rate)

print(f"The marginal cost of the combined cycle plant is ${marginal_cost:.2f} per MWh.")