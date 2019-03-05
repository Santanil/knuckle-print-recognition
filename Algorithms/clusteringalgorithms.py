import numpy as np
from scipy.spatial import distance
import time

# no of clusters is the cluster of 'n' images of single finger knuckle of single person

class ClusteringAlgorithms:

    def __init__(self,X):
        """
            X : {array-like, sparse matrix}                                               \
            Training data. If array or matrix, shape [n_samples, n_features],             \
            or [n_samples, n_samples] if metric=’precomputed’.                            \
        """
        self.input_array = X

    # Optimal Clustering Algorithm
    def OCA(self,n_clusters,threshold):
        """
            n_clusters : int                                                              \
            The number of clusters to form as well as the number of centroids to generate.\

            threshold : double                                                            \
            Threshold :Intra cluster distance i.e. distance between 2 images of a cluster.\
        """
        points = self.input_array
        dist = []
        value_of_points = np.zeros(shape = (n_clusters,1), dtype = float)

        # Create a cluster containing the first randomly selected point; mean of the cluster is equal to the value of the point
        clusters = []
        clusters.append([self.input_array[0]]) # initiating clusters(0) with first image
        # value_of_points[0] = np.mean(clusters[0][0])

        """ for each existing cluster ci do calculate the difference di between any randomly selected point not yet clustered and
            the current cluster means;"""
        for i in range(1,len(points)):
            for index in range(len(clusters)):
                print("calculating for cluster-",index+1)
                print("Image num: ",i+1)
                d= distance.euclidean(np.mean(clusters[index],axis=0),points[i]) # axis =0  means column wise .i.e, average row
                # print("Value of di calculated: ",di)
                # dist.append(di)
                # d = min(dist)
                print("Value of d: ",d)
                print("Sleeping...")
                print()
                time.sleep(4)
                print("Current no. of clusters: ",len(clusters))
                # print(clusters)
                if d <= threshold:
                    print()
                    print(d,"less than equal to",threshold)
                    print("inserting at : ",index+1,"-cluster")
                    clusters[index].append(points[i])
                    # print("Cluster[",index,"]: ",clusters[index])
                    print()
                    # value_of_points[index] = np.mean(clusters[index],axis=0)
                elif d > threshold:
                    print()
                    print(d,"greater than",threshold)
                    print("creating new cluster",index+2)
                    print()
                    clusters.append([points[i]])
                   # value_of_points[index+1] = np.mean(clusters[index+1])

        # for i in range(n_clusters):
        #     time.sleep(2)
        #     print(i,clusters[i])