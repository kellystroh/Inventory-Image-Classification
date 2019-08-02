import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline 

from sklearn.manifold import TSNE

df = pd.read_csv('data/full_labels_df.csv', error_bad_lines=False)
loaded = np.load('data/image_array.npz')
bw_img = loaded['b']
bw_img = bw_img/255
tsne2 = TSNE(n_components=2, n_iter=1000, perplexity=50, verbose=1)
XX = tsne2.fit_transform(bw_img)
np.save('tsne2.npy', XX)
