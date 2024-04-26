#File Discription: Create a graph that shows the highest bids compared to the marginal cost
#Author: Emily Deuchar

# January 2023 - March 2023 visualization: We chose 3 months at a time so that the data would be easier to see
import pandas as pd
import matplotlib.pyplot as plt

# Define a function to plot generator bids and marginal cost for a given date range
def plot_data(start_year, start_month, end_month, title):
    # Read the CSV file for generator bids into a DataFrame
    highest_block_prices_df = pd.read_csv('highest_block_prices_per_day.csv')

    # Convert the date column to a datetime object
    highest_block_prices_df['begin_dateTime_mpt'] = pd.to_datetime(highest_block_prices_df['begin_dateTime_mpt'])

    # Filter data for the specified date range
    data = highest_block_prices_df[
        (highest_block_prices_df['begin_dateTime_mpt'].dt.year == start_year) &
        (highest_block_prices_df['begin_dateTime_mpt'].dt.month >= start_month) &
        (highest_block_prices_df['begin_dateTime_mpt'].dt.month <= end_month)
    ]

    # Plot generator bids for each day of the specified date range
    for asset_id, group in data.groupby('asset_ID'):
        plt.scatter(group['begin_dateTime_mpt'], group['block_price'], label=f'Generator {asset_id}', marker='x')

    # Read the CSV file for marginal cost into a DataFrame
    marginal_cost_df = pd.read_csv('Marginal_cost_calculation.csv')
    marginal_cost_df['Date'] = pd.to_datetime(marginal_cost_df['Date'])

    # Filter marginal cost data for the specified date range
    marginal_cost_dates = marginal_cost_df[
        (marginal_cost_df['Date'].dt.year == start_year) &
        (marginal_cost_df['Date'].dt.month >= start_month) &
        (marginal_cost_df['Date'].dt.month <= end_month)
    ]

    # Plot marginal cost as 'x' markers
    plt.scatter(marginal_cost_dates['Date'], marginal_cost_dates['Calculated Value'], color='black', marker='x', label='Marginal Cost')

    # Set plot labels and title
    plt.xlabel('Year-Day-Month')
    plt.ylabel('Bid Amount')
    plt.title(title)

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

# Plot data for each quarter of the year 2023
plot_data(2023, 1, 3, 'Generator Bids from January to March 2023')
plot_data(2023, 4, 6, 'Generator Bids from April to June 2023')
plot_data(2023, 7, 9, 'Generator Bids from July to September 2023')
plot_data(2023, 10, 12, 'Generator Bids from October to December 2023')