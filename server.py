#Importing Libraries
from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import os
from facedetection import face_recognition_image
from extension import mycol

app = Flask(__name__)

#UPLOAD_FOLDER contains the path to which image from which face is to be detected is stored.
UPLOAD_FOLDER = os.getcwd() + '\img'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

#URL "localhost-address/imagesubmit" accepts both GET and POST requests and executes imagesubmit() function.
@app.route("/imagesubmit", methods=['GET', 'POST'])
#imagesubmit() function gets image from http POST request and passes that file name to face_recognition_image function.
def imagesubmit():
    if request.method == 'POST':
        f = request.files['Criminal_Image']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # After executing face_recognition_image function it stores Object_IDs of recognized faces in matches_id.
        matches_id = face_recognition_image(filename)
        #If length of matches_id is non zero then atleast one face is recognized from our database.
        if(len(matches_id)!=0):
            #people contains information about all criminals whose object_id is present in matches_id.
            people = mycol.find({"_id": { "$in" : matches_id} },{'image_encoding' : 0})
            people=list(people)
            #After fetching information about all the criminals we will display it on a webpage through render_template function.
            return render_template('view.html', people=people)
        #If length of matches_id is zero then no criminal is recognized from our database in given image.
        else:
            return render_template('noview.html')
    return "Failure"

from user.routes import bp

app.register_blueprint(bp)

#Here we are defining the home page route and it exectes home() function.
@app.route('/')
def home():
    return render_template('main.html')

#URL "localhost-address/insertcriminal" executes insertcriminal function .
#It takes us to webpage which displays a html form which accepts criminal information and stores it to our database.
@app.route("/insertcriminal")
def insertcriminal():
    return render_template('insert.html')

#URL "localhost-address/imagesurvillence" executes findcriminal function .
#It takes us to a webpage which accepts an image as an input from which face are to be recognized.
@app.route("/imagesurvillence")
def findcriminal():
    return render_template('find.html')


if __name__=="__main__":
    app.run(debug=True)