import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from full_df import df, all_img

from sklearn.decomposition import PCA

wearable_list = ['Apparel', 'Accessories', 'Footwear']
wearable_df = df[ df['masterCategory'].isin(wearable_list) ]
wearable_img = all_img[ wearable_df.index.values ].copy()

bw_wearables = wearable_img.reshape(-1, 80, 60, 3).mean(3).reshape(-1, 80*60)

pca = PCA(n_components=2)
bw_wearables_pca = pca.fit_transform(bw_wearables)

wearables_pca = pca.fit_transform(wearable_img)

masterCat_colors = {'Apparel':'orange','Accessories':'teal','Footwear':'red', 'Personal Care':'grey', 'Free Items':'yellow', 'Sporting Goods':'black', 'Home':'magenta'}
wearable_df['colors'] = wearable_df['masterCategory'].apply(lambda x: masterCat_colors[x])

fig, ax = plt.subplots(figsize=(6,6))
ax.scatter( *wearables_pca.T, s=.25 , color=wearable_df['colors'])
fig.savefig('fig6.png')