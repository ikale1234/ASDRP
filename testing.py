import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot
exo = pd.read_csv('goodexo.csv', low_memory=False)

print(exo.columns.tolist())

count = 0
for index, row in exo.iterrows():
  if pd.isna(row['st_mass']):
    pass
  else:
    count+=1
print(count)