# data-mining-hierarchical-clustering-
In this code we will be doing hierarchical clustering which is used in data mining 

## Supervised vs Unsupervised

when we are given a target variable (count and Survival in the above two cases) which we have to predict based on a given set of predictors or independent variables (season, holiday, Sex, Age, etc.), such problems are called supervised learning problems.

Here, y is our dependent or target variable, and X represents the independent variables. The target variable is dependent on X and hence it is also called a dependent variable. We train our model using the independent variables in the supervision of the target variable and hence the name supervised learning.

## Types of Clustering

![image](https://user-images.githubusercontent.com/63282184/134457458-2a8f77b6-3b56-476e-9d0b-a61d7cf90bc7.png)

## what is Hierarchical clustering ?

Hierarchical clustering, also known as hierarchical cluster analysis, is an algorithm that groups similar objects into groups called clusters.

The endpoint is a set of clusters, where each cluster is distinct from each other cluster, and the objects within each cluster are broadly similar to each other.

## How hierarchical clustering works
Hierarchical clustering starts by treating each observation as a separate cluster. Then, it repeatedly executes the following two steps: (1) identify the two clusters that are closest together, and (2) merge the two most similar clusters. 




**The Hierarchical Clustering can be dived into 2 types:**
1. Agglomerative Clustering
2. Divisive Clustering


## How do we measure the similarity between the clusters:

- Measuring the similarity between two clusters is important to merge or divide the clusters. 
- Some of the approaches which are used to calculate the similarity between two clusters are:

1. **MIN**
2. **MAX**
3. **Group Average**
4. **Distance Between Centroids**
5. **Ward’s Method**
