from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import os
from facedetection import face_recognition_image
from extension import mycol

app = Flask(__name__)

UPLOAD_FOLDER = os.getcwd() + '\img'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route("/imagesubmit", methods=['GET', 'POST'])
def imagesubmit():
    if request.method == 'POST':
        print(request.files)
        f = request.files['Criminal_Image']
        print(f)
        filename = secure_filename(f.filename)
        print(filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        matches_id = face_recognition_image(filename)
        print(matches_id)
        if(len(matches_id)!=0):
            people = mycol.find({"_id": { "$in" : matches_id} },{'image_encoding' : 0})
            for i in people:
                print(i)
            return render_template('view.ejs', people=people)
        else:
            return render_template('noview.html')
    return "Failure"

from user.routes import bp

app.register_blueprint(bp)

@app.route('/')
def home():
    return render_template('main.html')

@app.route("/insertcriminal")
def insertcriminal():
    return render_template('insert.html')

@app.route("/imagesurvillence")
def findcriminal():
    return render_template('find.html')


if __name__=="__main__":
    app.run(debug=True)