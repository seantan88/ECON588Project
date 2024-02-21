import pandas as pd


# read the csv files in chunks
chunksize = 10 ** 6  # adjust this value to fit your available memory
chunks = []

for chunk in pd.read_csv(r"C:\Users\seanh\Documents\GitHub\ECON588Project\CSV data\Merit Order Data\daily_merit_trim_asset.csv", chunksize=chunksize):
    # process each chunk here
    chunks.append(chunk)

df1 = pd.concat(chunks, axis=0)

# repeat for df2
chunks = []
for chunk in pd.read_csv(r"C:\Users\seanh\Documents\GitHub\ECON588Project\CSV data\CSD Data\CSD_Generation_2023.csv", chunksize=chunksize):
    chunks.append(chunk)

df2 = pd.concat(chunks, axis=0)

# merge the dataframes
df3 = pd.merge(df1, df2, left_on = 'asset_ID', right_on = 'Asset Short Name')

# drop unnecessary columns
df3 = df3[['block_price', 'Planning Area', 'asset_ID']]
df3 = df3.dropna()

# run a cluster analysis
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# create a dataframe with only the block_price and planning area columns
df4 = df3[['block_price', 'Planning Area']]
# create a list of the unique planning areas

planning_areas = df4['Planning Area'].unique()
# create a list of the unique asset_IDs
asset_IDs = df3['asset_ID'].unique()

# create a dictionary to store the cluster centers
cluster_centers = {}

# iterate through the unique asset_IDs

for asset in asset_IDs:
    # create a dataframe for each asset
    df5 = df4[df3['asset_ID'] == asset]
    # create a list to store the cluster centers
    centers = []
    # iterate through the unique planning areas
    for area in planning_areas:
        # create a dataframe for each planning area
        df6 = df5[df5['Planning Area'] == area]
        # create a numpy array from the block_price column
        X = df6['block_price'].values
        # reshape the array
        X = X.reshape(-1, 1)
        # run the KMeans algorithm
        kmeans = KMeans(n_clusters = 3)
        kmeans.fit(X)
        # append the cluster centers to the list
        centers.append(kmeans.cluster_centers_)
    # add the list of cluster centers to the dictionary
    cluster_centers[asset] = centers

# create a plot for each asset and planning area
for asset in asset_IDs:
    df5 = df4[df3['asset_ID'] == asset]
    for area in planning_areas:
        df6 = df5[df5['Planning Area'] == area]
        X = df6['block_price'].values
        X = X.reshape(-1, 1)
        kmeans = KMeans(n_clusters = 3)
        kmeans.fit(X)
        plt.scatter(X, kmeans.labels_)
        plt.scatter(kmeans.cluster_centers_, [0, 1, 2], c = 'red')
        plt.title(f'{asset} {area}')
        plt.show()




        



