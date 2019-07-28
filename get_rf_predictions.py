
def predict_master_cat(upload_array):
    #check if this is using the most recent rf pkl file location
    with open('../models_pkl/random_forest.pkl', 'rb') as fit_rf:
        clf = pickle.load(fit_rf)
    predicted_category = clf.predict(upload_array)
    probability = clf.predict_proba(upload_array)
    for i in range(len(yhat)):
        return (predicted_category, probability)
