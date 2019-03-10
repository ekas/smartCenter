import cv2
import numpy as np
import random
import string
import os
import sys
def adjust_gamma(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)
def record(file,name):
    capture = cv2.VideoCapture(file)
    k=0
    j=0
    newpath=os.path.join("data/VideoData",name)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    face_cascade_haar1 = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')
    while True:
        ret,frame=capture.read()
        width,height,ch=frame.shape

        # frame=cv2.resize(frame,(1200,1000))
        frame=adjust_gamma(frame,1.5)
        frame1=cv2.resize(frame,(640,480))
        rand=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces2 = face_cascade_haar1.detectMultiScale(frame_gray, 1.1, 9, 0, (50, 50), (600, 600))
        if j>3:
            if len(faces2) > 0:
                for x, y, w, h in faces2:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
                print(k)
                rand = str(rand) + '.jpg'

                cv2.imwrite(os.path.join(newpath, str(rand)), frame1)
                if k > 18:
                    break
                k += 1
        cv2.imshow('sdg', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        j+=1

    cv2.destroyAllWindows()

fileName=sys.argv[1]
Name=sys.argv[2]
if fileName=='live':
    record(0,Name)
else:
    record(fileName,Name)