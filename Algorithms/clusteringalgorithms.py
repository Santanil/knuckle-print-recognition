import numpy as np
from scipy.spatial import distance

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
        value_of_points = np.zeros(shape= 1, dtype = float)
        clusters = [[self.input_array[0]]] # initiating clusters(0) with first image
        value_of_points[0] = np.mean(clusters[0][0])

        # for cluster in clusters:
        #     cluster = np.array(cluster)

        # *INCOMPLETE DON'T FUCKING DARE TO TOUCH