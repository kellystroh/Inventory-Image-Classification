#toggle relevant models
with open('../models_pkl/random_forest.pkl', 'rb') as fit_rf:
    clf = pickle.load(fit_rf)

def predict_master_cat(upload_array):
    predicted_category = clf.predict(upload_array)
    probability = clf.predict_proba(upload_array)
    arr = np.zeros(len(probability), 2)
    for i in range(len(predicted_category)):
        arr[i,:] = [predicted_category[i], probability[i,predicted_category]]
    return arr
