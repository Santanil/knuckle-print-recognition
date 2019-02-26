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
        array_of_dist = []
        dist = []
        value_of_points = np.zeros(shape = (n_clusters,1), dtype = float)

        # Create a cluster containing the first randomly selected point; mean of the cluster is equal to the value of the point
        # clusters = np.zeros(shape = (n_clusters,1), dtype=int)
        clusters = [0] * n_clusters
        clusters[0] = [self.input_array[0]] # initiating clusters(0) with first image
        value_of_points[0] = np.mean(clusters[0][0])

        """ for each existing cluster ci do calculate the difference di between any randomly selected point not yet clustered and
            the current cluster means;"""
        for index in range(n_clusters):
            for point in self.input_array:
                cluster = np.array(clusters[index])
                di = distance.euclidean(np.mean(cluster),np.mean(point))
                # di = distance.euclidean([value_of_points[index]],point)
                print("Value of di calculated: ",di)
                dist.append(di)
                d = min(dist)
                print("Value of d: ",d)
                if d <= threshold:
                    clusters[index].append(point)
                    value_of_points[index] = np.mean(clusters[index])
                elif d > threshold:
                    clusters[index+1] = [point]
                    value_of_points[index+1] = np.mean(clusters[index+1])
            print("Sleeping...")
            time.sleep(5)

        for i in range(n_clusters):
            time.sleep(2)
            print(i,clusters[i],value_of_points[i])