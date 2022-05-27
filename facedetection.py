#Importing Libraries
import cv2
import os
import dlib
import face_recognition
import pymongo
import numpy as np

folder = "img"

#Function face_recognition_image takes file name as input which is present in directory stored in folder and recognises faces of criminals which are present in our database.
#It returns object_IDs of all the criminals whose faces are recognized in given image.
def face_recognition_image(filen):
    dst = f"{folder}/{filen}"
    face_cascade = cv2.CascadeClassifier('face_detector.xml')
    img =cv2.imread(dst)

    #Face-Recognition
    #boxes stores locations of faces present in img
    boxes=face_recognition.face_locations(img)
    #test_encode stores encodings of all the faces present in img.
    test_encode=face_recognition.face_encodings(img,boxes)

    from extension import mycol
    encoding=[]
    object_id=[]
    nm=[]
    #x stores data of all the criminals present in the database.
    x = mycol.find({},{'image_encoding': 1, 'name':1})
    for data in x:
        #object_id stores object ids of all the data stored.
        object_id.append(data["_id"])
        #encoding stores image encodings of all the images submitted.
        encoding.append(data["image_encoding"])
        #nm stores names of all the criminals whose information is stored in our database.
        nm.append(data["name"])

    Matched_IDs=[]
    for (top, right, bottom, left), face_encoding in zip(boxes, test_encode):
        #face_recognition.compare_faces function compares face_encoding with all the elements of encoding array.
        #It returns true if both of them matches false otherwise.
        matches = face_recognition.compare_faces(encoding, face_encoding,0.6)
        #face_recognition.face_distance tells us how similar the faces are.
        faceDist = face_recognition.face_distance(encoding, face_encoding)
        #matchIndex finds the index of most similar face from our batabase by finding index of minimum element of faceDist.
        matchIndex = np.argmin(faceDist)
        #If face at matchIndex matches with given encoding then we construct a rectangle around that face and name it.
        if matches[matchIndex]:
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(img, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            #Matched_IDs stores Object_ids of all recognized faces from our database.
            Matched_IDs.append(object_id[matchIndex])
            cv2.putText(img, nm[matchIndex], (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

    #We will now store the modified image as face_recognized.jpg in output_img folder of static folder.
    File_path=os.getcwd() + '\static\output_img'
    cv2.imwrite(os.path.join(File_path , "face_recognized.jpg"), img)
    #Since we don't require uploaded image now, we will now remove that image from our project.
    os.remove(dst)

    #We will return an array of object ids of recognized criminals.
    return Matched_IDs


