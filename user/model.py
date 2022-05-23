from flask import Flask,jsonify, request
import copy
#import server

class Criminal:

    def insertrecord(self):

        criminal={

            "name": request.form.get('Name'),
            "fname": request.form.get('Fathers_Name'),
            "DOB": request.form.get('Date'),
            "crime": request.form.get('Crimes_Commited'),
            "gender": request.form.get('gender')
        }

        old_criminal=copy.deepcopy(criminal)
        from extension import db
        mycol=db['Criminal']
        mycol.insert_one(criminal)

        return jsonify(old_criminal),200