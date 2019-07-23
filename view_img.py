import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def view_some_images(row_list, num, df='img_arr', colormode='c'):
    loaded = np.load('../image_array.npz')
    if colormode == 'c':
        img_arr = loaded['a']
    else:
        img_arr = loaded['b']

    if type(num) is tuple:
        sample = np.random.randint(0, len(row_list), size=(num[0]*num[1]))
        ht= num[0]*2.5
        wd= num[1]*1.67
    else:
        sample = np.random.randint(0, len(row_list), size=num)
        ht= 2.5
        wd= num*1.67

    fig, axs = plt.subplots(*num, figsize=(wd, ht))
    for i, ax in enumerate(axs.flatten()):
        ax.imshow( df[sample[i]].reshape(80,60,3)/255 )
        ax.set_xticks([])
        ax.set_yticks([])

def view_these_images(row_list, num, df='img_arr', colormode='c'):
    