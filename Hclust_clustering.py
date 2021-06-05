import pandas as pd
import matplotlib.pylab as plt

data1 = pd.read_excel(" ") #give your file pat
data1.describe()
data1.info()

data = data1.drop([" "], axis=1) # if you wish to drop any column we can enter the column name in the blank space

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)


df_norm = norm_func(data.iloc[:, 1:])
df_norm.describe()

# dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z = linkage(df_norm, method = "complete", metric = "euclidean") # here i have chossen euclidean but we can choose other distance methods also

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()


# AgglomerativeClustering 
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(df_norm) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

data['clust'] = cluster_labels # creating a new column and assigning it to new column 

data1 = data.iloc[:, [7,0,1,2,3,4,5,6]]
data1.head()

# Aggregate mean 
data1.iloc[:, 2:].groupby(data1.clust).mean()

# saving the output into csv file 
data1.to_csv("data.csv", encoding = "utf-8")

import os
os.getcwd()
