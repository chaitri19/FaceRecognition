#Importing Libraries
from flask import Flask,request,Blueprint,render_template
from user.model import Criminal

bp=Blueprint('criminal',__name__)

#URL "localhoat-address/criminal" executes criminalrecord function.
@bp.route('/criminal',methods=['POST'])
def criminalrecord():
    criminal=Criminal()
    criminal.insertrecord()
    #After inserting data to our database we will go to our home page.
    return render_template("main.html")
