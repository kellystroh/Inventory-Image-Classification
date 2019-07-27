from werkzeug import secure_filename
from flask import Flask, request, render_template
import os, os.path

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

# @app.route('/account', methods=['GET'])
# def account():
#     return render_template('account.html')

@app.route('/account', methods=['GET'])
def upload_file():
    return render_template('account.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['upload_folder'], secure_filename(f.filename)))
      return render_template('account.html')
		
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8087, debug=True)


'''
photo creds: 
#7
Photo by Artem Beliaikin on Unsplash

girl in closet #2
Photo by Becca McHaffie on Unsplashmv 

hanging clothes
Photo by Priscilla Du Preez on Unsplash

chair #4
Photo by Sarah Dorweiler on Unsplash

hats #8 
Photo by David Vilches on Unsplash

door #9
Photo by Artem Beliaikin on Unsplash

#10
Photo by Ashim D’Silva on Unsplash
'''