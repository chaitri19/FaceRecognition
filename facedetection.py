import cv2
import os
import dlib
import face_recognition
import pymongo
import numpy as np

folder = "img"

def face_recognition_image(filen):
    dst = f"{folder}/{filen}"
    face_cascade = cv2.CascadeClassifier('face_detector.xml')
    img =cv2.imread(dst)

    #Face-Recognition
    boxes=face_recognition.face_locations(img)
    test_encode=face_recognition.face_encodings(img,boxes)

    from extension import mycol
    encoding=[]
    object_id=[]
    print("--------------")
    x = mycol.find({},{'image_encoding': 1})
    for data in x:
        object_id.append(data["_id"])
        encoding.append(data["image_encoding"])

    Matched_IDs=[]
    for (top, right, bottom, left), face_encoding in zip(boxes, test_encode):
        matches = face_recognition.compare_faces(encoding, face_encoding,0.6)
        faceDist = face_recognition.face_distance(encoding, face_encoding)
        matchIndex = np.argmin(faceDist)
        if matches[matchIndex]:
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(img, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            Matched_IDs.append(object_id[matchIndex])
            cv2.putText(img, "Face", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    File_path=os.getcwd() + '\static\output_img'
    cv2.imwrite(os.path.join(File_path , "face_recognized.jpg"), img)
    os.remove(dst)
    print('Successfully saved')

    return Matched_IDs


