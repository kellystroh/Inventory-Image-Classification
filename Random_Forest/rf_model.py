import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import dill as pickle
np.random.seed(33) # My childhood soccer number



# Load the CSV file containing category labels
df_train = pd.read_csv('data/train_labels.csv')
df_test = pd.read_csv('data/test_labels.csv')

# Load the NPZ with image array data; 
loaded = np.load('data/bw_images.npz')
X_train = loaded['a']
X_test = loaded['b']

# Generate categorical labels for master categories by assigning 
# numbers (0 to 3) to each category, in alphabetical order. 
y_train = df_train.masterCategory.copy()
y_train = y_train.astype('category')
y_train = y_train.cat.codes

y_test = df_test.masterCategory.copy()
y_test = y_test.astype('category')
y_test = y_test.cat.codes

# Fit Random Forest Classifier
clf = RandomForestClassifier(n_estimators = 100, random_state=33)
clf.fit(X_train, y_train)

# Pickle fit model for analytics in Jupyter Notebook
with open('models_pkl/random_forest.pkl', 'wb') as f:
    pickle.dump(clf, f)