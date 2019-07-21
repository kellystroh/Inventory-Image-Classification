import numpy as np
import pandas as pd
import imageio
import glob

# import kaggle dataset 
df = pd.read_csv('/home/ubuntu/Clothing-Clusters/data/styles.csv', error_bad_lines=False)
## df = pd.read_csv('~/galvanize/week8/data/styles.csv', error_bad_lines=False)
df.set_index('id', inplace=True)

# get list of file names for images
path = r'/home/ubuntu/Clothing-Clusters/data/images' 
#path# = r'/Users/Kelly/galvanize/week8/data/images'

files = glob.glob(path + "/*.jpg")
idx_series = pd.Series(files, dtype=object).str.replace('/home/ubuntu/Clothing-Clusters/data/images/', '').str.replace('.jpg', '')
## idx_series = pd.Series(files, dtype=object).str.replace('/Users/Kelly/galvanize/week8/data/images/', '').str.replace('.jpg', '')

pic_arr = np.array(files)
## pic_arr = np.array(files)[0:100]

def get_pixels(files):
    r = np.zeros((len(files),14400))
    for i in range(len(files)):
        img = imageio.imread(files[i])
        flat = np.array(img).flatten()
        if len(flat) == 14400:   
            r[i,:] = flat  
    return r

def problematic_images(files):
    bad_list = []
    for i in range(len(files)):
        img = imageio.imread(files[i])
        flat = np.array(img).flatten()
        if len(flat) != 14400:   
            bad_list.append(files[i])
    return bad_list

# make clothing df
images_arr = get_pixels(pic_arr)

pic_df0 = pd.DataFrame(images_arr, index=idx_series.astype(int), dtype='int')
## pic_df0 = pd.DataFrame(images_arr, index=idx_series[0:100].astype(int), dtype='int')
pic_df = pic_df0[pic_df0.notnull()]

pic_idx = set(pic_df.index)
df_idx = set(df.index)

# include only items present in BOTH indices
df = df[df.index.isin(pic_idx)]
pic_df = pic_df[pic_df.index.isin(df_idx)]

'''
#double check this is True:
pic_idx = df_idx
'''
def make_subset_wearable(df, pic_df):
    # make a wearable subset
    wearable_list = ['Apparel', 'Accessories', 'Footwear']
    wearable_df = df[df['masterCategory'].isin(wearable_list)]

    wear_idx = list(wearable_df.index)
    wear_pics = pic_df[pic_df.index.isin(wear_idx)]
    if set(wear_pics.index) == set(wearable_df.index):
        return wear_pics
    else: 
        return "You Done Messed Up Now"

def make_subset_apparel(df, pic_df):
    apparel_df = df[df['masterCategory']=='Apparel']
    apparel_idx = list(apparel_df.index)
    apparel_pics = pic_df[pic_df.index.isin(apparel_idx)]
    if set(apparel_pics.index) == set(apparel_df.index):
        return apparel_pics
    else: 
        return "You Done Messed Up Now"

# print(wear_pics.head())
# print(images_arr.shape)
# double check this is True
# set(wear_pics.index) == set(wearable_df.index)