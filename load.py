import numpy as np
import pandas as pd
import imageio
import glob
from zipfile import ZipFile 


'''
/Users/Kelly/anaconda3/lib/python3.7/site-packages/numpy/core/_methods.py:36: RuntimeWarning: overflow encountered in reduce
  return umr_sum(a, axis, dtype, out, keepdims, initial)
'''


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
bw_float64 = all_img.reshape(-1, 80, 60, 3).mean(3).reshape(-1, 80*60)
bw_img = bw_float64.astype('float16')

### find bad images
bad_rows_idx = np.where(bw_img.sum(axis=1)==0)[0].tolist()
every_row_idx = list(range(44446))
keep_rows_idx = list(set(every_row_idx)-set(bad_rows_idx))

### exclude bad images
X1 = all_img[keep_rows_idx, :]
X2 = bw_img[keep_rows_idx, :]

df = df[~df.index.isin(bad_rows_idx)].reset_index(drop=True)

df.to_csv('data/labels_df.csv', index=False)
print('df saved')
np.savez_compressed('data/image_array', a=X1, b=X2)
print('array saved')