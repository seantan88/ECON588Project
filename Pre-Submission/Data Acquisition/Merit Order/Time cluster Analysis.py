import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Define a function to perform cluster analysis on bid times
def cluster_analysis(start_year, start_month, end_month, title, n_clusters):
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

    # Extract hour of the day
    data['Hour'] = data['begin_dateTime_mpt'].dt.hour

    # Perform cluster analysis
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data[['Hour']])
    data['Cluster'] = kmeans.predict(data[['Hour']])

    # Plot cluster analysis
    plt.scatter(data['Hour'], data['block_price'], c=data['Cluster'], cmap='viridis')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Bid Amount')
    plt.title(title)
    plt.colorbar(label='Cluster')
    plt.show()

# Perform cluster analysis for each quarter of the year 2023
cluster_analysis(2023, 1, 3, 'Cluster Analysis of Generator Bids from January to March 2023', 3)
cluster_analysis(2023, 4, 6, 'Cluster Analysis of Generator Bids from April to June 2023', 3)
cluster_analysis(2023, 7, 9, 'Cluster Analysis of Generator Bids from July to September 2023', 3)
cluster_analysis(2023, 10, 12, 'Cluster Analysis of Generator Bids from October to December 2023', 3)