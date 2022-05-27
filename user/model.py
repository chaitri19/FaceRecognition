#Importing Libraries
from flask import Flask
from flask import jsonify
from flask import request
from werkzeug.utils import secure_filename
import os
import cv2
import copy
import cv2
import os
import dlib
import face_recognition

class Criminal:

    #Function insertrecord accepts data from http post request and processes it and stores it to our database.
    def insertrecord(self):

        f = request.files['Insert_Criminal']
        filename = secure_filename(f.filename)
        #We will first store image to our project directory and then find its facial encodings which is stored in our database.
        f.save(filename)
        img = cv2.imread(filename)
        try:
            #train_image stores facial encodings of uploaded image.
            train_image = face_recognition.face_encodings(img)[0]
        except IndexError as e:
            print(e)
            os.remove(filename)
            quit()
        

        criminal={

            "name": request.form.get('Name'),
            "fname": request.form.get('Fathers_Name'),
            "DOB": request.form.get('Date'),
            "crime": request.form.get('Crimes_Commited'),
            "gender": request.form.get('gender'),
            "image_encoding": [train_image[i] for i in range(len(train_image))],
            "imark": request.form.get('i_mark')
        }

        old_criminal=copy.deepcopy(criminal)
        from extension import mycol
        mycol.insert_one(criminal)
        #Since we stored facial encodings of image we don't require image any more.
        os.remove(filename)
        return jsonify(old_criminal),200