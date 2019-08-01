from werkzeug import secure_filename
from flask import Flask, request, render_template
import os, os.path
from get_rf_predictions import predict_master_cat
from preprocess_uploads import process_images
#from config import Config
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)


app_root = os.path.dirname(os.path.abspath(__file__))
upload_fold = '/Users/Kelly/galvanize/capstone/website/image_uploads'
upload_folder = os.path.join(app_root, upload_fold)
app.config['upload_folder'] = upload_folder


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/account', methods=['GET'])
def upload_file():
    return render_template('account.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    uploaded_files = request.files.getlist("file[]")
    for f in uploaded_files:
        f.save(os.path.join(app.config['upload_folder'], secure_filename(f.filename)))
    return render_template('iam.html')

def get_data():
    X = process_images('image_uploads')
    data = predict_master_cat(X, '../json/cnn-main.h5')
    return data

def write_json_file(filename, data):
    try:
        with open(filename, "w") as f:
            f.writelines(data)
        print(filename + " has been created.")
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    filename = 'json_file.json'
    data = get_data()
    write_json_file(filename, data)
    app.run(host='0.0.0.0', port=8880, debug=True)





'''
photo creds: 
#7 Photo by Artem Beliaikin on Unsplash
girl in closet #2 Photo by Becca McHaffie on Unsplashmv 
hanging clothes Photo by Priscilla Du Preez on Unsplash
chair #4 Photo by Sarah Dorweiler on Unsplash
hats #8 Photo by David Vilches on Unsplash
door #9 Photo by Artem Beliaikin on Unsplash
#10 Photo by Ashim D’Silva on Unsplash
# 11 Photo by Lauren Fleischmann on Unsplash
'''