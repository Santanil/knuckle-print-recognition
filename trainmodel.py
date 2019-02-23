# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Algorithms.clusteringalgorithms import ClusteringAlgorithms

from parse_config import ParseConfig

configparser = ParseConfig()
if 'datasetPath' in configparser.configs.keys():
    datasetAbsPath = configparser.configs['datasetPath']
else:
    print("Check config")
    exit(-1)


# Importing the dataset
dataset = pd.read_csv(datasetAbsPath, header=None)
X = dataset.values

# calculating and printing no.of image samples
num_of_image_samples_in_matrix = len(dataset.index)
# print(num_of_image_samples_in_matrix)

num_of_images_per_fingerknuckle = 6
# print(num_of_images_per_fingerknuckle)
total_number_of_clusters =int(num_of_image_samples_in_matrix / num_of_images_per_fingerknuckle)
print("Total number of clusters taken:", total_number_of_clusters)

clusteralgoObj = ClusteringAlgorithms(X)
clusters  = clusteralgoObj.OCA(total_number_of_clusters,threshold = 70)
# print((clusters[0][0]))