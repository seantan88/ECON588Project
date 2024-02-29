import pandas as pd


df1 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/CSD Data/CSD Generation (Hourly) - 2023-01 to 2023-06.csv")
df2 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Merit Order Data/Monthly Data/daily_merit_first6mos.csv")

# rename Asset Short Name to 'asset_ID' in df1
df1.rename(columns = {'Asset Short Name': 'asset_ID'}, inplace = True)
# rename Date (MPT) to 'begin_dateTime_mpt' in df1
df1.rename(columns = {'Date (MPT)': 'begin_dateTime_mpt'}, inplace = True)
# drop unnecessary columns in df1
df1 = df1[['begin_dateTime_mpt', 'asset_ID', 'System Capability']]
# merge the two dataframes on the 'asset_ID' and 'begin_dateTime_mpt' columns
df3 = pd.merge(df1, df2, on = ['asset_ID', 'begin_dateTime_mpt'], how = 'inner')





# drop unnecessary columns
df3 = df3[['begin_dateTime_mpt','block_price', 'System Capability', 'asset_ID']]
# drop any rows with NaN values
df3 = df3.dropna()
# save the combined dataframe to a csv file
df3.to_csv('CSD_Merit_2023.csv')

# run a cluster analysis
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt



# perform the elbow method to determine the optimal number of clusters
# create a list of inertia values for each number of clusters
inertia = []
# loop through the number of clusters from 1 to 10
for i in range(1, 11):
    # create a kmeans model
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    # fit the model to the features
    kmeans.fit(df3[['block_price', 'System Capability']])
    # append the inertia value to the list
    inertia.append(kmeans.inertia_)


# plot the inertia values
#plt.plot(range(1, 11), inertia)
# add labels
#plt.title('Elbow Method')
#plt.xlabel('Number of clusters')
#plt.ylabel('Inertia')
# show the plot
#plt.show()
    
    ## RESULT OF ELBOW METHOD: 3 CLUSTERS ##









# fit the kmeans model to the features, using 3 clusters
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
# fit the model to the features
kmeans.fit(df3[['block_price', 'System Capability']])
# add a new column to df3 that contains the cluster labels
df3['cluster'] = kmeans.labels_
# create new figure
plt.figure()

# plot the clusters
plt.scatter(df3['block_price'], df3['System Capability'], c = kmeans.labels_, cmap = 'viridis')
# plot the centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'red')
# add the generator ids to the plot so we can see which generators are in each cluster
#for i in range(len(df3['asset_ID'])):
    #plt.text(df3['block_price'][i], df3['System Capability'][i], df3['asset_ID'][i])
# add labels
plt.title('Clusters of Generators')
plt.xlabel('Block Price ($)')
plt.ylabel('System Capability (MW)')
# show the plot
plt.show()












        


