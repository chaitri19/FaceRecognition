import cv2
import numpy as np
import PIL.Image
import dlib
import face_recognition

#munipuli@microsoft.com
recogface= face_recognition.load_image_file("Resouces/images/input.jpg")
imgelon_bgr = face_recognition.load_image_file('Resources/images/input.jpg')
imgelon_rgb = cv2.cvtColor(imgelon_bgr,cv2.COLOR_BGR2RGB)
cv2.imshow('bgr', imgelon_bgr)
cv2.imshow('rgb', imgelon_rgb)
cv2.waitKey(0)