import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import imageio
import glob

df = pd.read_csv('data/styles.csv', error_bad_lines=False)


all_img = []
for i, ix in enumerate( df.id ):
    if i%1000==0:
        print(i, len(df))
    
    fn = r'data/images/{}.jpg'.format(ix)
    try:
        img = imageio.imread(fn)
        if img.shape!=(80, 60, 3):
            all_img.append( [0]*(60*80*3) )
        else:
            all_img.append( img.ravel() )
    except FileNotFoundError:
        all_img.append( [0]*(60*80*3) )

all_img = np.stack(all_img)
bw_img = all_img.reshape(-1, 80, 60, 3).mean(3).reshape(-1, 80*60)

