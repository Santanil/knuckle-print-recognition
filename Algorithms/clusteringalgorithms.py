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
        # dist = []
        # value_of_points = np.zeros(shape = (n_clusters,1), dtype = float)
        clusters = [] # Create a cluster containing the first randomly selected point; mean of the cluster is equal to the value of the point
        clusters.append([self.input_array[0]]) # initiating clusters(0) with first image
        """ for each existing cluster ci do calculate the difference di between any randomly selected point not yet clustered and
            the current cluster means;
        """
        for i in range(1,len(points)):
            for index in range(len(clusters)):
                print("\nCalculating for cluster-",index+1)
                print("Image num: ",i+1)

                d = distance.euclidean(np.mean(clusters[index],axis=0),points[i]) # axis =0  means column wise

                # print("\nValue of di calculated: ",di)
                # dist.append(di)
                # d = min(dist)

                print("\nValue of d: ",d)
                print("\n\nSleeping...\n")
                time.sleep(3)

                print("Current no. of clusters: ",len(clusters))

                if d <= threshold:
                    clusters[index].append(points[i])
                    print("\n",d," less than equal to ",threshold)
                    print("\nInserting at :cluster-",index+1)

                elif d > threshold:
                	clusters.append([points[i]])