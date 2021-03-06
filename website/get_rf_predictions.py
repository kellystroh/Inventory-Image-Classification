#toggle relevant models
# with open('../models_pkl/random_forest.pkl', 'rb') as fit_rf:
#     clf = pickle.load(fit_rf)



def predict_master_cat(upload_array, model_loc):
    from tensorflow.keras.models import Sequential, load_model
    import numpy as np
    import pandas as pd
   
    model = load_model(model_loc)

    predicted_category = model.predict(upload_array)
    #print(type(predicted_category))
    probability = model.predict_proba(upload_array)
    probability = np.round(probability, 3)
    # list_cat = []
    # list_prob = []
    df = pd.DataFrame(probability, columns=['Accessory', 'Apparel','Footwear','Personal Care'])
    df.insert(0, 'Prediction', df.idxmax(axis=1))
    
    #df['Prediction'] = predicted_category.transpose()

    # for i in range(len(predicted_category)):
    #     print(type(predicted_category[i]))
    #     print(predicted_category[i].shape)
    #     t = predicted_category[i]
    #     list_cat.append(t)
    #     list_prob.append(probability[i])
    return df
