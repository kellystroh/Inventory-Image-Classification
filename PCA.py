import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('data/full_labels_df.csv')
loaded2 = np.load('data/full_image_arr.npz')
image_arr = loaded2['b']
image_arr = image_arr/255

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

full_pca = pca.fit_transform(image_arr)
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(*full_pca.T, s=.1 )

masterCat_colors = {'Apparel':'#FF6347','Accessories':'#48D1CC','Footwear':'#FFA500', 'Personal Care': 'black'}
# {'Personal Care':'#808080', 'Free Items':'#808080', 'Sporting Goods':'#808080', 'Home':'#808080'}
df['colors'] = df['masterCategory'].apply(lambda x: masterCat_colors[x])
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter( *full_pca.T, s=.1 , color=df['colors'])

fig.savefig('PCA_master.png')