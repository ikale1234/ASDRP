import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot
exo = pd.read_csv('goodexo.csv', low_memory=False)
print(exo.columns.tolist())
exo_2 = exo[['pl_orbper', 'pl_dens', 'pl_radj']].copy()
print(exo_2)

km = KMeans(n_clusters =3)
count = 0
exo_good = exo[['pl_name', 'pl_orbper', 'pl_eqt', 'pl_orbeccen', 'st_rad', 'pl_imppar', 'pl_orbincl', 'pl_insol', 'pl_ratdor', 'pl_trandep']].copy()
for index, row in exo_good.iterrows():
  if pd.isna(row['pl_orbper'])  or pd.isna(row['pl_eqt']) or pd.isna(row['pl_orbeccen']) or pd.isna(row['st_rad']) or pd.isna(row['pl_imppar']) or pd.isna(row['pl_orbincl']) or pd.isna(row['pl_insol']) or pd.isna(row['pl_ratdor']) or pd.isna(row['pl_trandep']):
    exo_good = exo_good.drop(index)
  else:
    count+=1
print(count)
print(exo_good)
exo_good.to_csv("exoplanet1.csv")
# pyplot.scatter(exo_2['pl_orbper'], exo_2['pl_radj'])
# pyplot.show()