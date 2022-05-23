from flask import Flask,request,render_template,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.getcwd() + '\img'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route("/imagesubmit", methods=['GET', 'POST'])
def imagesubmit():
    if request.method == 'POST':
        print(request.files)
        f = request.files['Criminal_Image']
        filename = secure_filename(f.filename)
        print(filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return("Home")
    return ("Failure")

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