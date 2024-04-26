#File Discription: Difference between the block price and the marginal cost
#Author: Emily Deuchar

import pandas as pd
import matplotlib.pyplot as plt

# Define a function to plot the difference between bid price and marginal cost for each asset
def plot_difference_by_asset(start_year, start_month, end_month, title):
    # Read the CSV file for highest daily generator bids into a DataFrame
    highest_block_prices_df = pd.read_csv('highest_block_prices_per_day.csv')

    # Convert the date column to a datetime object
    highest_block_prices_df['begin_dateTime_mpt'] = pd.to_datetime(highest_block_prices_df['begin_dateTime_mpt'])

    # Filter data for the specified date range
    data = highest_block_prices_df[
        (highest_block_prices_df['begin_dateTime_mpt'].dt.year == start_year) &
        (highest_block_prices_df['begin_dateTime_mpt'].dt.month >= start_month) &
        (highest_block_prices_df['begin_dateTime_mpt'].dt.month <= end_month)
    ]

    # Read the CSV file for marginal cost into a DataFrame
    marginal_cost_df = pd.read_csv('Marginal_cost_calculation.csv')
    marginal_cost_df['Date'] = pd.to_datetime(marginal_cost_df['Date'])

    # Filter marginal cost data for the specified date range
    marginal_cost_dates = marginal_cost_df[
        (marginal_cost_df['Date'].dt.year == start_year) &
        (marginal_cost_df['Date'].dt.month >= start_month) &
        (marginal_cost_df['Date'].dt.month <= end_month)
    ]

    # Merge dataframes on 'Date' to get the corresponding marginal cost for each bid date
    merged_data = pd.merge(data, marginal_cost_dates, how='left', left_on='begin_dateTime_mpt', right_on='Date')

    # Calculate the difference between 'block_price' and 'Calculated Value' for each asset
    for asset_id, group in merged_data.groupby('asset_ID'):
        group['Difference'] = group['block_price'] - group['Calculated Value']
        plt.scatter(group['begin_dateTime_mpt'], group['Difference'], label=f'Asset {asset_id}', marker='x')

    # Set plot labels and title
    plt.xlabel('Year-Day-Month')
    plt.ylabel('Difference')
    plt.title(title)
    plt.legend()
    plt.show()

# Plot the difference for each quarter of the year 2023
plot_difference_by_asset(2023, 1, 3, 'Difference between Bid Amount and Marginal Cost from January to March 2023')
plot_difference_by_asset(2023, 4, 6, 'Difference between Bid Amount and Marginal Cost from April to June 2023')
plot_difference_by_asset(2023, 7, 9, 'Difference between Bid Amount and Marginal Cost from July to September 2023')
plot_difference_by_asset(2023, 10, 12, 'Difference between Bid Amount and Marginal Cost from October to December 2023')



