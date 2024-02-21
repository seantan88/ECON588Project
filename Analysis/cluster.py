import pandas as pd


df1 = pd.read_csv(r"C:\Users\seanh\Documents\GitHub\ECON588Project\CSV data\CSD Data\CSD Generation (Hourly) - 2023-01 to 2023-06.csv")
df2 = pd.read_csv(r"C:\Users\seanh\Documents\GitHub\ECON588Project\CSV data\Merit Order Data\Monthly Data\daily_merit_first6mos.csv")

# want to reame Asset Short Name to 'asset_ID' in df1
df1.rename(columns = {'Asset Short Name': 'asset_ID'}, inplace = True)
# merge the two dataframes
df3 = pd.merge(df1, df2, on = 'asset_ID')



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

from sklearn.cluster import KMeans

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
        # check if X is not empty
        if X.size > 0:
            print(X)
            # reshape the array
            X = X.reshape(-1, 1)
            # run the KMeans algorithm
            kmeans = KMeans(n_clusters = 3)
            kmeans.fit(X)
            # append the cluster centers to the list
            centers.append(kmeans.cluster_centers_)
        else:
            print(f"No data for asset {asset} in planning area {area}")
    # add the list of cluster centers to the dictionary
    cluster_centers[asset] = centers

# create a plot for each asset and planning area
for asset in asset_IDs:
    df5 = df4[df3['asset_ID'] == asset]
    for area in planning_areas:
        df6 = df5[df5['Planning Area'] == area]
        X = df6['block_price'].values
        if X.size > 0:
            X = X.reshape(-1, 1)
            kmeans = KMeans(n_clusters = 3)
            kmeans.fit(X)
            plt.scatter(X[:, 0], [area]*len(X), c=kmeans.labels_)
            plt.scatter(kmeans.cluster_centers_, [area]*3, c='red')
        else:
            print(f"No data for asset {asset} in planning area {area}")
    plt.title(f'{asset}')
    plt.show()




        



