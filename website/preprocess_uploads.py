def process_images(directory):
    from PIL import Image
    from skimage import transform,io, color
    from os import listdir
    import numpy as np
    upload_array = []
    pic_list = [f for f in listdir(directory) if f.endswith('.png')]

    for pic in pic_list:
        fn = r'{}/{}'.format(directory, pic)
        img = io.imread(fn)
        img = transform.rescale(img, 3.0 / 4.0, anti_aliasing=False)
        if img.shape[2]==4:
            img = color.rgba2rgb(img)
            
        img_new = transform.resize(img, (80,60,3))
        upload_array.append(img_new.ravel())

    all_uploads = np.stack(upload_array)
    bw_uploads = all_uploads.reshape(-1, 80, 60, 3).mean(3).reshape(-1, 80*60).astype('float16') 
    #all_uploads = all_uploads.reshape(-1,80,60,3)
    bw_uploads = bw_uploads.reshape(-1,80,60,1)
    return bw_uploads

# fig, axs = plt.subplots(1,3, figsize=(16,16))
# for i, ax in enumerate(axs.flatten()):
#     ax.imshow( all_uploads[i].reshape(80,60,3)  )
#     ax.set_xticks([])
#     ax.set_yticks([])
# plt.subplots_adjust(hspace = 0.7)


# def fix_dims(img):
#     ht = img.shape[0]
#     wd = img.shape[1]
#     ch = img.shape[2]
#     if wd/ht > 60/80:
#         if (wd*4)%3==1:
#             img = np.insert(img,0,[255,255,255],axis=1)
#             img = np.insert(img,0,[255,255,255],axis=1)
#             wd += 2
#         elif (wd*4)%3==2:
#             img = np.insert(img,0,255,axis=1)
#             wd += 1
#         rows_needed = int(wd*4/3 - ht)
#         #print(rows_needed)
#         rows1 = rows_needed//2 
#         rows2 = rows_needed - rows1
#         stack1 = np.ones([rows1,wd,3])
#         #print(stack1.shape)
#         stack2 = np.ones([rows2,wd,3])
#         #print(stack2.shape)
#         img_new = np.concatenate((stack1, img, stack2), axis=0)
#         return img_new
#     else:
#         if (ht*3)%4==1:
#             img = np.insert(img,0,[255,255,255],axis=0)
#             img = np.insert(img,0,[255,255,255],axis=0)
#             img = np.insert(img,0,[255,255,255],axis=0)
#             ht += 3
#             #print(img.shape)
#         if (ht*3)%4==2:
#             img = np.insert(img,0,[255,255,255],axis=0)
#             img = np.insert(img,0,[255,255,255],axis=0)
#             ht += 2
#             #print(img.shape)
#         elif (ht*3)%4==3:
#             img = np.insert(img,0,[255,255,255],axis=0)
#             ht += 1
#             #print(img.shape)
#         cols_needed = int(ht*3/4 - wd)
#         #print('cols_needed',cols_needed)
#         cols1 = cols_needed//2 
#         cols2 = cols_needed - cols1
#         stack1 = np.ones([ht,cols1,3])
#         #print('stack1',stack1.shape)
#         stack2 = np.ones([ht,cols2,3])
#         #print('stack2',stack2.shape)
#         img_new = np.concatenate((stack1, img, stack2), axis=1)
#         return img_new