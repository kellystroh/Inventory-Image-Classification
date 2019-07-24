import numpy as np
import pandas as pd
import imageio
import glob
from zipfile import ZipFile 

#my childhood soccer number
np.random.seed(33)




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
'''
Warning will appear because we are 'losing info' by converting from float64 to 
float16... the higher degree of precision is not needed. 
/Users/Kelly/anaconda3/lib/python3.7/site-packages/numpy/core/_methods.py:36: RuntimeWarning: overflow encountered in reduce
  return umr_sum(a, axis, dtype, out, keepdims, initial)
'''

### find load-error images
bad_rows_idx = np.where(bw_img.sum(axis=1)==0)[0].tolist()
every_row_idx = list(range(44446))
keep_rows_idx = list(set(every_row_idx)-set(bad_rows_idx))

### exclude load-error images
X1 = all_img[keep_rows_idx, :]
X2 = bw_img[keep_rows_idx, :]

df = df[~df.index.isin(bad_rows_idx)].reset_index(drop=True)

### remove unneeded categories
malo_category = ['Free Items', 'Sporting Goods', 'Home']
malo_idx = list(df[df.masterCategory.isin(malo_category)].index)
#malo_df = df[df.masterCategory.isin(malo_category)]
df = df[~df.masterCategory.isin(malo_category)]
bw_img = np.delete(bw_img, malo_idx, 0)
all_img = np.delete(all_img, malo_idx, 0)

### test train split
shuffle = np.random.choice( np.arange(len(bw_img)), size=len(bw_img), replace=False)
X_bw = bw_img[shuffle]
X_color = all_img[shuffle]
y = labels.values[shuffle]

n_train = round(len(X_bw)*.70)
n_val = round(len(X_bw)*.90)

images_train_bw = X_bw[:n_train]
images_train_color = X_color[:n_train]
labels_train = y[:n_train]
shuffle_train = shuffle[:n_train]

images_test_bw = X_bw[n_train:n_val]
images_test_color = X_color[n_train:n_val]
labels_test = y[n_train:n_val]
shuffle_test = shuffle[n_train:n_val]

images_final_bw = X_bw[n_val:]
images_final_color = X_color[n_val:]
labels_final = y[n_val:]
shuffle_final = shuffle[n_val:]

y.to_csv('data/labels_df.csv', index=False)
print('full df saved')
labels_train.to_csv('data/train_labels.csv', index=False)
print('train df saved')
labels_test.to_csv('data/test_labels.csv', index=False)
print('test df saved')
labels_test.to_csv('data/final_labels.csv', index=False)
print('final df saved')


np.savez_compressed('data/shuffle_arrays', a=shuffle_train, b=shuffle_test, c=shuffle_final)
print('full array saved')
np.savez_compressed('data/color_images', a=images_test_color, b=images_train_color, c=images_final_color)
print('color array saved')
np.savez_compressed('data/bw_images', a=images_test_bw, b=images_train_bw, c=images_final_bw)
print('bw array saved')