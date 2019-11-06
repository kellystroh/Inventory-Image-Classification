
def process_images(directory):
    from PIL import Image
    from skimage import transform,io
    from os import listdir
    import numpy as np
    upload_array = []
    pic_list = [f for f in listdir(directory) if f.endswith('.png')]

    for pic in pic_list:
        fn = r'{}/{}'.format(directory, pic)
        img = io.imread(fn)
        img = transform.rescale(img, 3.0 / 4.0, anti_aliasing=False)
        if img.shape[2]==4:
            img = rgba2rgb(img)
            
        img_new = transform.resize(img, (80,60,3))
        upload_array.append(img_new.ravel())

    all_uploads = np.stack(upload_array)
    bw_uploads = all_uploads.reshape(-1, 80, 60, 3).mean(3).reshape(-1, 80*60).astype('float16')   
    return (all_uploads, bw_uploads)

def predict_master_cat(upload_array):
    with open('models_pkl/rfc_master.pkl', 'rb') as fit_model:
        model = pickle.load(fit_model)    
    predicted_category = model.predict(upload_array)
    probability = model.predict_proba(upload_array)
    arr = np.zeros(len(probability), 2)
    for i in range(len(predicted_category)):
        arr[i,:] = [predicted_category[i], probability[i,predicted_category]]
    return arr

def predictions_to_SQL(data):
    from database import db_session
    from models import Item
    
    new = Item('admin', 'admin@localhost')
    db_session.add(new)
    db_session.commit()

    return 





