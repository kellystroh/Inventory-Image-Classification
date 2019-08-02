This project explores how machine learning can be utilized by online retailers with collections of inventory photos. I utilized a dataset published on Kaggle, with 44,000 product images (80 x 60 pixels). My time in Scotland tells me these images come from a British Department store, but this is simply a Scottish-educated guess. A corresponding table provided details about the item featured in each image, including a main category, sub-category, article type, and base color. The data cleaning process involved removing groups with too few images and combining duplicate sub-categories. These steps narrowed the data to a mere 32,000 images. After downloading the images and labels from Kaggle, you can use the file load.py to generate the datasets I used. 

Exploratory analysis began with dimension reduction and hierarchical clustering. For each of these approaches, I utilized the flattened, greyscale pixel values. Each image was represented by one row of 4,800 columns. I used PCA and t-SNE to reduce the image data to two dimensions, in order to visualize the differences between images. See Jupyter notebooks (PCA.ipynb & tsne.ipynb) for specifics. The hierarchical clustering component needs further exploration. Results suggested some recognition of main categories, but additional work is needed to identify image characteristics of the clusters. 





