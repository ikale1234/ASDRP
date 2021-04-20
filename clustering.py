import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot
exo = pd.read_csv('exoplanet1.csv', low_memory=False)
print(exo)