import numpy as np
import pandas as pd
import imageio

#my childhood soccer number
np.random.seed(33)

df = pd.read_csv('../data/styles.csv', error_bad_lines=False)

'''

After some exploration of the data, I determined that there are several 
changes to the data that will improve the performance of our image classifier. 

Most of the changes are related to the consistency of categories. 
Example : 'Socks' is a sub-category under both Apparel and Accessories in original
data, so I edited the 'masterCategory' column to combine these into one sub-category
within the main category 'Apparel'.

While a department store may have reason to have similar items in separate 
departments, it is preferable for our purposes to have similar items grouped in 
one category. 


'''
socks= list(df[df.subCategory=='Socks'].index)
df.iloc[socks, 2] = 'Apparel'

# Move all items within 'Perfume' sub-categories into Personal Care 
# and set sub-category value to 'Fragrance'
perfumes= list(df[df.subCategory=='Perfumes'].index)
df.iloc[perfumes, 2] = 'Personal Care'
df.iloc[perfumes, 3] = 'Fragrance'

# Combine the Personal Care sub-categories of 'Eyes' & 'Makeup' 
# because the article types overlap
eyes = list(df[df.subCategory=='Eyes'].index)
df.iloc[eyes,3] = 'Makeup'

# If the sub-category is 'Shoe' and the article type is flip flops, 
# move item into the sub-category 'Flip Flops'
flops = list(df[df.articleType=='Flip Flops'].index)
df.iloc[eyes,3] = 'Flip Flops'

# If the sub-category is 'Shoe' and the article type is sandals,
# move item into the sub-category 'Sandals'
sandals = (df[df.articleType=='Sandals'].index)
df.iloc[eyes,3] = 'Sandals'

# combine similar colors
peach = (df[df.baseColour=='Peach'].index)
df.iloc[peach, 5] = 'Orange'

purple = list(df[df.baseColour == 'Lavender'].index)
df.iloc[purple, 5] = 'Purple'

cream = ['Beige', 'Off White']
cream_idx = (df[df.baseColour.isin(cream)].index)
df.iloc[cream_idx, 5] = 'Cream'

red = ['Rust', 'Burgundy', 'Maroon', 'Magenta']
red_idx = list(df[df.baseColour.isin(red)].index)
df.iloc[red_idx, 5] = 'Red'

pink = ['Mauve', 'Rose']
pink_idx = list(df[df.baseColour.isin(pink)].index)
df.iloc[pink_idx, 5] = 'Pink'

tan = ['Nude', 'Skin', 'Taupe', 'Khaki']
tan_idx = list(df[df.baseColour.isin(tan)].index)
df.iloc[tan_idx, 5] = 'Tan'

brown = ['Mushroom Brown', 'Coffee Brown', 'Mustard', 'Gold']
brown_idx = list(df[df.baseColour.isin(brown)].index)
df.iloc[brown_idx, 5] = 'Brown'

green = ['Lime Green', 'Olive']
green_idx = list(df[df.baseColour.isin(green)].index)
df.iloc[green_idx, 5] = 'Green'

blue = ['Turquoise Blue', 'Teal', 'Sea Green']
blue_idx = list(df[df.baseColour.isin(blue)].index)
df.iloc[blue_idx, 5] = 'Blue'

grey = ['Charcoal', 'Grey Melange', 'Silver']
grey_idx = list(df[df.baseColour.isin(grey)].index)
df.iloc[grey_idx, 5] = 'Grey'


def filter_article(mast_cat, line):
    items = df[df.masterCategory==mast_cat].groupby(['subCategory','articleType']).count().id
    num_drop = len(items[items < line])
    drop_list = []
    for i in range(num_drop):
        c = items[items < line].index[i][1]
        drop_list.append(c)
    return drop_list

all_img = []
for i, ix in enumerate( df.id ):
    if i%2000==0:
        print(i, len(df))

    fn = r'../data/images/{}.jpg'.format(ix)
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

RuntimeWarning: overflow encountered in reduce return umr_sum(a, axis, dtype, out, keepdims, initial)
'''
#np.savez_compressed('data/original_image_arr.npz', a=all_img, b=bw_img)

### find load-error images
bad_rows_idx = np.where(bw_img.sum(axis=1)==0)[0].tolist()
every_row_idx = list(range(44446))
keep_rows_idx = list(set(every_row_idx)-set(bad_rows_idx))

### exclude load-error images
all_img = all_img[keep_rows_idx, :]
bw_img = bw_img[keep_rows_idx, :]

df = df[~df.index.isin(bad_rows_idx)].reset_index(drop=True)
# print(X1.shape)
# print(X2.shape)
print(df.shape)
### remove unneeded categories
malo_category = ['Free Items', 'Sporting Goods', 'Home']
malo_idx = list(df[df.masterCategory.isin(malo_category)].index)
print(len(malo_idx))
malo_df = df[df.masterCategory.isin(malo_category)]
print(malo_df.shape)
df = df[~df.masterCategory.isin(malo_category)].reset_index(drop=True)
bw_img = np.delete(bw_img, malo_idx, 0)
all_img = np.delete(all_img, malo_idx, 0)

### remove sub-categories with n < 150
short_list = ['Accessories', 'Scarves', 'Apparel Set', 'Cufflinks', 'Stoles', 'Skin Care', 
              'Skin','Mufflers', 'Shoe Accessories', 'Hair', 'Gloves', 'Bath and Body',
              'Water Bottle', 'Umbrellas', 'Beauty Accessories', 'Sports Accessories']
short_idx = list(df[df.subCategory.isin(short_list)].index)
print('filter sub-categories with n < 150, # rows removed: ', len(short_idx))
print('# sub-cats removed: ', len(short_list))
df = df[~df.subCategory.isin(short_list)].reset_index(drop=True)
bw_img = np.delete(bw_img, short_idx, 0)
all_img = np.delete(all_img, short_idx, 0)

### remove article-types with n < 30
app_drop_list = filter_article('Apparel', 30)
acc_drop_list = filter_article('Accessories', 30)
pc_drop_list = filter_article('Personal Care', 30)
drop_list = app_drop_list + acc_drop_list + pc_drop_list
drop_idx = list(df[df.articleType.isin(drop_list)].index)
print('filter article-types with n < 30; # row removed: ',len(drop_idx))
print('# article-types removed: ', len(drop_list))
df = df[~df.articleType.isin(drop_list)].reset_index(drop=True)
bw_img = np.delete(bw_img, drop_idx, 0)
all_img = np.delete(all_img, drop_idx, 0)

### remove childrens categories 
kid_list = ['Girls', 'Boys']
kid_idx = (df[df.gender.isin(kid_list)].index)
df = df[~df.gender.isin(kid_list)]
bw_img = np.delete(bw_img, kid_idx, 0)
all_img = np.delete(all_img, kid_idx, 0)

print('df', df.shape)
print('all', all_img.shape)
print('bw', bw_img.shape)
np.savez_compressed('../data/full_image_arr.npz', a=all_img, b=bw_img)
print('full arr saved')
df.to_csv('../data/full_labels_df.csv', index=False)
print('full df saved')

### test train split
shuffle = np.random.choice( np.arange(len(bw_img)), size=len(bw_img), replace=False)
print(shuffle.shape)
X_bw = bw_img[shuffle]
X_color = all_img[shuffle]
y = df.iloc[shuffle,:]

n_train = round(len(X_bw)*.75)
n_val = round(len(X_bw)*.95)

images_train_bw = X_bw[:n_train]
images_train_color = X_color[:n_train]
labels_train = y[:n_train]
shuffle_train = shuffle[:n_train]

images_test_bw = X_bw[n_train:n_val]
images_test_color = X_color[n_train:n_val]
labels_test = y[n_train:n_val]
shuffle_test = shuffle[n_train:n_val]

images_val_bw = X_bw[n_val:]
images_val_color = X_color[n_val:]
labels_val = y[n_val:]
shuffle_val = shuffle[n_val:]



labels_train.to_csv('../data/train_labels.csv', index=False)
print('train df saved')
labels_test.to_csv('../data/test_labels.csv', index=False)
print('test df saved')
labels_val.to_csv('../data/val_labels.csv', index=False)
print('final df saved')


np.savez_compressed('../data/shuffle_arrays.npz', a=shuffle_train, b=shuffle_test, c=shuffle_val, d=shuffle)
print('full array saved')
np.savez_compressed('../data/color_images.npz', a=images_train_color, b=images_test_color, c=images_val_color)
print('color array saved')
np.savez_compressed('../data/bw_images.npz', a=images_train_bw, b=images_test_bw, c=images_val_bw)
print('bw array saved')
