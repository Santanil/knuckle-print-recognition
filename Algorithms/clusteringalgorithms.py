import numpy as np
from scipy.spatial import distance
import time
import logging
from  apputility import printProgressBar

# logger initialization
logging.basicConfig(filename='doubcheck.log', filemode='w', format='%(asctime)s: %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger()

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
        # value_of_points = np.zeros(shape = (n_clusters,1), dtype = float)
        clusters = []
        clusters.append([points[0]]) # initiating clusters(0) with first image
        """ for each existing cluster ci do calculate the difference di between any randomly selected point not yet clustered and
            the current cluster means;
        """
        # Initial call to print 0% progress
        # printProgressBar(0, n_clusters, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i in range(1, len(points)):
            cleardistornot = i % 6 # hard coded to 6 for now since we are taking 6 images
            if 0 == cleardistornot:
                dist.clear()
            for ci in clusters:
                di = distance.euclidean(np.mean(ci,axis=0),points[i]) # axis =0  means column wise
                if 0.0 != di:
                    dist.append(di)
                    d = min(dist)
                    if d <= threshold:
                        ci.append(points[i])

                    else:
                        # creating new cluster and inserting there
                        clusters.append([points[i]])

            # printProgressBar(index + 1, n_clusters, prefix = 'Progress:', suffix = 'Complete', length = 50)
