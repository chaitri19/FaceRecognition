import cv2
import os

folder = "img"
for count, filename in enumerate(os.listdir(folder)):
    dst = f"i-{str(count)}.jpg"
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"

    os.rename(src, dst)

face_cascade = cv2.CascadeClassifier('face_detector.xml')
img =cv2.imread("img\i-0.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30),
    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

# Draw rectangle around the faces
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 100, 0), 2)

File_path=os.getcwd() + '\output_img'
cv2.imwrite(os.path.join(File_path , "face_detected.png"), img) 
print('Successfully saved')

#os.remove("img\i-0.jpg")