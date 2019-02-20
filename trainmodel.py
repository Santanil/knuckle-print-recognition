# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance
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
no_of_clusters = 2
clusters = [[None]] * no_of_clusters

def OCA(input_arr,thresh):
     # confirm with mam how to choose the proper no. of clusters
    X = input_arr
    
    global clusters
    # selecting first image to find euclidean distance with
    # other images in X aka. input_arr
    clusters[0]  = X[0] # clusters[i] is also a list
    clusters[-1] =X[-1]
    try:
        for i in range(0, no_of_clusters):
            for sample in X[1:-1]:
                dist = distance.euclidean(clusters[i], sample)
                if dist < thresh:
                    np.append(clusters[0],sample)
                    print(clusters[0])
                    
                elif dist > thresh:
                    np.append(clusters[-1],sample)
                    
    except Exception as e:
        print(e)
        pass

OCA(X,70)