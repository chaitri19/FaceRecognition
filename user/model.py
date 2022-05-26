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

    def insertrecord(self):

        f = request.files['Insert_Criminal']
        filename = secure_filename(f.filename)
        print(os.getcwd())
        print(filename)
        f.save(filename)
        print("File Saved")
        img = cv2.imread(filename)
        print(len(img))
        try:
            train_image = face_recognition.face_encodings(img)[0]
            print(len(train_image))
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
            "image_encoding": [train_image[i] for i in range(len(train_image))]
        }

        old_criminal=copy.deepcopy(criminal)
        from extension import mycol
        mycol.insert_one(criminal)
        os.remove(filename)
        return jsonify(old_criminal),200