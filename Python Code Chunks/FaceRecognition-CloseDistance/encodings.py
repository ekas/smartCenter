import os
import face_recognition
import pickle
import sys
import cv2
from sklearn.svm import SVC
import numpy as np

def adjust_gamma(image, gamma):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

def justEncode():
     f = open ("encodingsVideo.dat","wb")
     for i in range(0,len(folderList)):
        temp = os.listdir(os.path.join(imgFolder,folderList[i]))
        print (i)
        index=0
        for imgName in temp:

            name = os.path.join(imgFolder,folderList[i],imgName)
            # print (name)
            if index>=0:
                # print(index, name)
                index += 1
                img_bgr = cv2.imread(name)
                width,height,ch=img_bgr.shape
                if width>1200:
                    img_bgr = cv2.resize(img_bgr, (480, 640))
                # print (img_bgr.shape)
                img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                img_gamma1 = adjust_gamma(img_gray, 0.5)
                img_gamma2 = adjust_gamma(img_gray, 1)
                img_gamma3 = adjust_gamma(img_gray, 1.5)
                img_gamma4 = adjust_gamma(img_gray, 2)

                img_gamma1_cntrst1 = clahe1.apply(img_gamma1)
                img_gamma1_cntrst2 = clahe2.apply(img_gamma1)
                img_gamma1_cntrst3 = clahe3.apply(img_gamma1)

                img_gamma2_cntrst1 = clahe1.apply(img_gamma2)
                img_gamma2_cntrst2 = clahe2.apply(img_gamma2)
                img_gamma2_cntrst3 = clahe3.apply(img_gamma2)

                img_gamma3_cntrst1 = clahe1.apply(img_gamma3)
                img_gamma3_cntrst2 = clahe2.apply(img_gamma3)
                img_gamma3_cntrst3 = clahe3.apply(img_gamma3)

                img_gamma4_cntrst1 = clahe1.apply(img_gamma4)
                img_gamma4_cntrst2 = clahe2.apply(img_gamma4)
                img_gamma4_cntrst3 = clahe3.apply(img_gamma4)

                img_gamma1_cntrst1 = cv2.cvtColor(img_gamma1_cntrst1, cv2.COLOR_GRAY2RGB)
                img_gamma1_cntrst2 = cv2.cvtColor(img_gamma1_cntrst2, cv2.COLOR_GRAY2RGB)
                img_gamma1_cntrst3 = cv2.cvtColor(img_gamma1_cntrst3, cv2.COLOR_GRAY2RGB)

                img_gamma2_cntrst1 = cv2.cvtColor(img_gamma2_cntrst1, cv2.COLOR_GRAY2RGB)
                img_gamma2_cntrst2 = cv2.cvtColor(img_gamma2_cntrst2, cv2.COLOR_GRAY2RGB)
                img_gamma2_cntrst3 = cv2.cvtColor(img_gamma2_cntrst3, cv2.COLOR_GRAY2RGB)

                img_gamma3_cntrst1 = cv2.cvtColor(img_gamma3_cntrst1, cv2.COLOR_GRAY2RGB)
                img_gamma3_cntrst2 = cv2.cvtColor(img_gamma3_cntrst2, cv2.COLOR_GRAY2RGB)
                img_gamma3_cntrst3 = cv2.cvtColor(img_gamma3_cntrst3, cv2.COLOR_GRAY2RGB)

                img_gamma4_cntrst1 = cv2.cvtColor(img_gamma4_cntrst1, cv2.COLOR_GRAY2RGB)
                img_gamma4_cntrst2 = cv2.cvtColor(img_gamma4_cntrst2, cv2.COLOR_GRAY2RGB)
                img_gamma4_cntrst3 = cv2.cvtColor(img_gamma4_cntrst3, cv2.COLOR_GRAY2RGB)

                img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
                if width>700 and width<1250:
                    faces = face_cascade_haar.detectMultiScale(img_gray, 1.1, 15, 0, (1, 1), (800, 800))

                else:
                    faces = face_cascade_haar.detectMultiScale(img_gray, 1.1, 11, 0, (50, 50), (600, 600))
                if len(faces) > 0:
                    for x, y, w, h in faces:
                        loc = [y, x + w, y + h, x]
                        loca = list(zip(loc))
                        for k in range(3):
                            loca[0] = (loca[0] + loca[k + 1])
                        face_encodings1 = face_recognition.face_encodings(img_gamma1_cntrst1, [loca[0]])
                        face_encodings2 = face_recognition.face_encodings(img_gamma1_cntrst2, [loca[0]])
                        face_encodings3 = face_recognition.face_encodings(img_gamma1_cntrst3, [loca[0]])
                        face_encodings4 = face_recognition.face_encodings(img_gamma2_cntrst1, [loca[0]])
                        face_encodings5 = face_recognition.face_encodings(img_gamma2_cntrst2, [loca[0]])
                        face_encodings6 = face_recognition.face_encodings(img_gamma2_cntrst3, [loca[0]])
                        face_encodings7 = face_recognition.face_encodings(img_gamma3_cntrst1, [loca[0]])
                        face_encodings8 = face_recognition.face_encodings(img_gamma3_cntrst2, [loca[0]])
                        face_encodings9 = face_recognition.face_encodings(img_gamma3_cntrst3, [loca[0]])
                        face_encodings10 = face_recognition.face_encodings(img_gamma4_cntrst1, [loca[0]])
                        face_encodings11 = face_recognition.face_encodings(img_gamma4_cntrst2, [loca[0]])
                        face_encodings12 = face_recognition.face_encodings(img_gamma4_cntrst3, [loca[0]])

                        if len(face_encodings1):
                            s_face_encodings.append(face_encodings1[0])
                            label.append(folderList[i])
                        if len(face_encodings2):
                            s_face_encodings.append(face_encodings2[0])
                            label.append(folderList[i])
                        if len(face_encodings3):
                            s_face_encodings.append(face_encodings3[0])
                            label.append(folderList[i])
                        if len(face_encodings4):
                            s_face_encodings.append(face_encodings4[0])
                            label.append(folderList[i])
                        if len(face_encodings5):
                            s_face_encodings.append(face_encodings5[0])
                            label.append(folderList[i])
                        if len(face_encodings6):
                            s_face_encodings.append(face_encodings6[0])
                            label.append(folderList[i])
                        if len(face_encodings7):
                            s_face_encodings.append(face_encodings7[0])
                            label.append(folderList[i])
                        if len(face_encodings8):
                            s_face_encodings.append(face_encodings8[0])
                            label.append(folderList[i])
                        if len(face_encodings9):
                            s_face_encodings.append(face_encodings9[0])
                            label.append(folderList[i])
                        if len(face_encodings10):
                            s_face_encodings.append(face_encodings10[0])
                            label.append(folderList[i])
                        if len(face_encodings11):
                            s_face_encodings.append(face_encodings11[0])
                            label.append(folderList[i])
                        if len(face_encodings12):
                            s_face_encodings.append(face_encodings12[0])
                            label.append(folderList[i])



     print ("Encoding complete \n Writing to file")
     trainData = [s_face_encodings,label]
     pickle.dump(trainData,f )
     f.close();
     
folder=str(sys.argv[1])
imgFolder=folder
print (imgFolder)


folderList = os.listdir(imgFolder)
imgs = []
s_image = []
s_face_encodings = []
label = []
face_cascade_haar = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')
clf = SVC(kernel='linear', probability=True, tol=1e-3)
print (folderList)
clahe1 = cv2.createCLAHE(clipLimit=1, tileGridSize=(16,16))
clahe2 = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(16,16))
clahe3 = cv2.createCLAHE(clipLimit=2, tileGridSize=(16,16))    
justEncode()
