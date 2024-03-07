# File Description: Cluster algorithm for electricity generation data
# Author: Sean Tan



# TODO
# - Get estimated marginal cost
# - Trim data to off-peak hours?
# - Reduce timeframe? or sort out messy labels
#   - Possibly monthly cluster?

# run a cluster analysis
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df3 = pd.read_csv(r"/Users/seantan88/Documents/GitHub/ElectricityCluster/CSV data/Combined Data/CSD_Merit_2023.csv")

# standardize the range of the continuous initial variables so that each one of them contributes equally to the analysis
# standardization is the process of subtracting the mean of each variable and then dividing by the standard deviation
# this makes the mean of each variable 0 and the standard deviation 1
# this is important for the k-means algorithm to work properly
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# fit the scaler to the features
scaler.fit(df3[['block_price', 'System Capability']])
# transform the features
df3[['block_price', 'System Capability']] = scaler.transform(df3[['block_price', 'System Capability']])
# check the results
#print(df3.head())

# compute the covariance matrix of the standardized variables
cov_matrix = np.cov(df3[['block_price', 'System Capability']].T)
print(cov_matrix)

# Compute the eigenvectors and eigenvalues of the covariance matrix to identify the principal components
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
#print(eigenvalues)
#print(eigenvectors)

#Create a Feature Vector
# sort the eigenvalues in descending order
eigenvalues_sorted = np.sort(eigenvalues)[::-1]
# sort the eigenvectors according to the sorted eigenvalues
eigenvectors_sorted = eigenvectors[:, eigenvalues.argsort()[::-1]]
# print the sorted eigenvectors
#print(eigenvectors_sorted)

# choose the number of principal components
# the number of principal components is the number of dimensions of the data
# we can choose the number of principal components based on the explained variance
# the explained variance tells us how much information (variance) can be attributed to each of the principal components
# we can calculate the explained variance by dividing each eigenvalue by the sum of all eigenvalues
explained_variance = eigenvalues_sorted / sum(eigenvalues_sorted)
print(explained_variance)

# plot the explained variance
plt.plot(np.cumsum(explained_variance))
# add labels
plt.title('Explained Variance')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
# show the plot
plt.show()

#use the feature vector formed using the eigenvectors of the covariance matrix, to reorient the data from the original axes to the ones represented by the principal components

# create the projection matrix
#projection_matrix = (eigenvectors_sorted.T[:][:2]).T
# project the data
#X_pca = df3[['block_price', 'System Capability']].dot(projection_matrix)
# create a new dataframe with the principal components
#df3 = pd.DataFrame(data = X_pca, columns = ['PC1', 'PC2'])



# plot the data
#plt.figure()
# plot the principal components
#plt.scatter(df3['PC1'], df3['PC2'])
# add labels
#plt.title('Principal Components')
#plt.xlabel('PC1')
#plt.ylabel('PC2')
# show the plot
#plt.show()














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
plt.plot(range(1, 11), inertia)
# add labels
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
# show the plot
plt.show()
    
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
plt.colorbar(label= 'Cluster')
plt.xlabel('Block Price ($)')
plt.ylabel('System Capability (MW)')
# show the plot
plt.show()



# plot a heat map of the block prices and system capabilities
plt.figure()
# create a pivot table of the data
pivot = df3.pivot_table(index = 'block_price', columns = 'System Capability', values = 'cluster', aggfunc = 'count')
# create the heat map
sns.heatmap(pivot, cmap = 'viridis')
# add labels
plt.title('Heat Map of Generators')
plt.xlabel('System Capability (MW)')
plt.ylabel('Block Price ($)')
# show the plot
#plt.show()

















        


