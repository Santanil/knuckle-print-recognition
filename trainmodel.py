# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from parse_config import ParseConfig

configparser = ParseConfig()
if 'datasetPath' in configparser.configs.keys():
    datasetAbsPath = configparser.configs['datasetPath']

# Importing the dataset
dataset = pd.read_csv(datasetAbsPath, header=None)
X = dataset.values