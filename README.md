### Streamlining Online Retail Inventory

This project explores how machine learning can be utilized by online retailers with collections of inventory photos. **This repo is a work in progress.** All sections are currently in need of updated notes, and updated relative links because of organizational changes. Below, I'll keep lists of the sections that are ready for use, as well as the upcoming additions. 

#### Dataset
I used a dataset published on Kaggle, with 44,000 product images (80 x 60 pixels). My time in Scotland tells me these images come from a British Department store, but this is simply a Scottish-educated guess. A corresponding table provided details about the item featured in each image, including a main category, sub-category, article type, and base color. The data cleaning process involved removing groups with too few images and combining duplicate sub-categories. These steps narrowed the data to a mere 32,000 images. 

#### How to run 
The sub-directories largely function independent of the others and can be done in any order, **except** for the two steps.

1. [**Download the data**](https://www.kaggle.com/paramaggarwal/fashion-product-images-small)
Once decompressed, the data from Kaggle should appear as an image folder and a CSV.   If you want to avoid editing filepaths, make a sub-directory called 'data' in this repo. Place the Kaggle downloads in the data folder, as a folder called 'images' and a CSV called 'styles.csv'.

2. **Run load.py file** 
After downloading the images and labels from Kaggle, you can use the file **load.py** to generate the datasets I used.

#### Current Status 
Ready to run:
* Process_Images
* CNN_Classifier
* Clustering

Under revision:
* Random_Forest
* Website





