# import os
import face_recognition
import pickle
import cv2
import dlib
from collections import Counter
# from imutils import face_utils
from sklearn.svm import SVC
import sys
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
import numpy as np
from scipy.spatial import distance as dist

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3

COUNTER = 0
TOTAL = 0

def adjust_gamma(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)

def onlyCloseDist(filename):
    clf2 = SVC(kernel='linear', probability=True, tol=1e-3)
    face_cascade_haar = cv2.CascadeClassifier('Cascades/haarcascade_profileface.xml')
    face_cascade_haar1 = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')
    f=open("Model-CloseDistVid.dat","rb")
    clf2 = pickle.load(f)


    final_name = []
    neck_dir = []
    face_names = []
    face_proba = []


    capture = cv2.VideoCapture(filename)

    j = 0

    while True:

        # Grab a single frame of video

        ret, frame = capture.read()
        # frame1 = frame.copy()
        # frame1 = cv2.flip(frame1, 1)

        # print (frame.shape)
        small_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # small_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

        small_frame = adjust_gamma(small_frame, 2.0)
        rgb_small_frame = frame[:, :, ::-1]

        # small_frame1 = adjust_gamma(small_frame1, 2.0)
        # rgb_small_frame1 = frame1[:, :, ::-1]
        small_frame=clahe2.apply(small_frame)
        # faces = face_cascade_haar.detectMultiScale(small_frame, 1.1, 7, 0, (50, 50), (600, 600))
        # faces1 = face_cascade_haar.detectMultiScale(small_frame1, 1.1, 7, 0, (50, 50), (600, 600))
        faces2 = face_cascade_haar1.detectMultiScale(small_frame, 1.1, 9, 0, (50, 50), (600, 600))
        if len(faces2) > 0:
            for x, y, w, h in faces2:
                # print (w,h)
                # print ((w-50)/150.0)
                #threshold=np.exp((w-50)/(150.0))/3.1#6.3
                threshold=0
                print (threshold)
                loc = [y, x + w, y + h, x]
                loca = list(zip(loc))
                l1, l2 = [], []
                neck_dir.append("front")
                for i in range(3):
                    loca[0] = (loca[0] + loca[i + 1])


                face_encodings = face_recognition.face_encodings(rgb_small_frame, [loca[0]])

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                face_names = []
                name = "Unknown"
                if face_encodings:
                    face_pred = clf2.predict(face_encodings)
                    face_proba = clf2.predict_proba(face_encodings)

                    name = face_pred
                    print (max(face_proba[0]),name)
                if max(face_proba[0]) > threshold:
                    face_names.append(name)
                    final_name.append(str(name))
                    cv2.putText(frame, str(name), (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

                else:
                    face_names.append("unknown")
                    final_name.append("unknown")
                    cv2.putText(frame, "unknown", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

        j += 1
        # if j > 30:
        #     break


        cv2.imshow('Video', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if len(final_name)==0:
        return ('unknow')
    counter = Counter(final_name)
    counter = counter.most_common()
    direc = Counter(neck_dir).values()
    # print (counter)
    return (counter[0][0])

clahe2 = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(16,16))

file=sys.argv[1]
if file=='live':
    name=onlyCloseDist(0)
else:
    name=onlyCloseDist(file)
print (name)