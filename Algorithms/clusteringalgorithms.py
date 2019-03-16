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
        points = self.input_array[:12]
        dist = []
        # value_of_points = np.zeros(shape = (n_clusters,1), dtype = float)
        clusters = [ [] for i in range(n_clusters) ] # Create a cluster containing the first randomly selected point; mean of the cluster is equal to the value of the point
        clusters[0].append(self.input_array[0]) # initiating clusters(0) with first image
        """ for each existing cluster ci do calculate the difference di between any randomly selected point not yet clustered and
            the current cluster means;
        """
        # Initial call to print 0% progress
        printProgressBar(0, 2, prefix = 'Progress:', suffix = 'Complete', length = 50)
        # for each cluster
        for index in range(2):
            # for each image/point
            for i in range(1,len(points)):
                logging.info("Processing Image num: "+str(i)+" for cluster-"+str(index))
                di = distance.euclidean(np.mean(clusters[index],axis=0),points[i]) # axis =0  means column wise
                # di = distance.euclidean(points[0],points[i]) # axis =0  means column wise
                logging.warning("Value of di: "+str(di))
                # print("\nValue of di calculated: ",di)
                dist.append(di)
                d = min(dist)
                logging.warning(di-d)
                if di-d <= threshold:
                    clusters[index].append(points[i])
                    logging.info(str(di-d)+" less than equal to "+str(threshold))
                    logging.info("Inserting at :cluster-"+str(index))

                elif di-d > threshold:
                    clusters[index+1].append(points[i])
                    logging.info("Inserting at :cluster-"+str(index+1))
                    logging.info(str(di-d)+" greater than equal to "+str(threshold))
            printProgressBar(index + 1, 2, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # print(len(clusters))
        # for index in range(n_clusters):
        #     print(len(clusters[index]))
