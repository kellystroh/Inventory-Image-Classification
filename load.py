import numpy as np
import pandas as pd
import imageio
import glob
from zipfile import ZipFile 

df = pd.read_csv('data/styles.csv', error_bad_lines=False)


all_img = []
for i, ix in enumerate( df.id ):
    if i%2000==0:
        print(i, len(df))

    fn = r'data/data/images/{}.jpg'.format(ix)
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

np.savez_compressed('data/image_array', a=all_img, b=bw_img)
