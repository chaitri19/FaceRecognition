from flask import Flask,request,Blueprint,render_template,redirect,url_for,current_app
import os
from werkzeug.utils import secure_filename
from user.model import Criminal
#from server import app

bp=Blueprint('criminal',__name__)
#UPLOAD_FOLDER = os.getcwd() + '/img'
#current_app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER



@bp.route('/criminal',methods=['POST'])
def criminalrecord():
    criminal=Criminal()
    criminal.insertrecord()
    return render_template("main.html")

@bp.route('/find-criminal',methods=['POST','GET'])
def findcriminalrecord():
    return ("Home")

#@bp.route("/imagesubmit", methods=['GET', 'POST'])
#def imagesubmit():
    #if request.method == 'POST':
        #if 'file' not in request.files:
            #print("File Not Present")
        #else:
            #print("IF statement executed")
            #f = request.files['Criminal_Image']
            #filename = secure_filename(f.filename)
            #f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('findciminalrecord'))
            #return("Home")
    #return render_template('find.html')
    #print(request.form.get('submit'))
    #print("Else statement executed")
    #return ("Failure")

#@app.route('/criminal',methods=['GET'])
#def criminalrecord():
    #criminal=Criminal()
    #return criminal.insertrecord(request.get_data())
    #return ("Home")

