#Create a merit order of highest bids at each hour:
#Author: Emily Deuchar
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a dataframe
highest_hourly_prices_df = pd.read_csv('highest_block_prices_hourly.csv')

# Convert the date column to a datetime object
highest_hourly_prices_df['begin_dateTime_mpt'] = pd.to_datetime(highest_hourly_prices_df['begin_dateTime_mpt'])

# Filter data for January 1st, 2023
january_1st_data = highest_hourly_prices_df[highest_hourly_prices_df['begin_dateTime_mpt'].dt.date == pd.to_datetime('2023-01-01').date()]

# Create a scatter plot for each generator's bids for each hour of January 1st, 2023
for asset_id, group in january_1st_data.groupby('asset_ID'):
    plt.scatter(group['begin_dateTime_mpt'], group['block_price'], label=f'Generator {asset_id}', marker='x')

# Set plot labels and title
plt.xlabel('Hour of January 1st, 2023')
plt.ylabel('Bid Prices')
plt.title('Generator Bids for Each Hour of January 1st, 2023')

# Add legend
plt.legend()

# Show the plot
plt.show()