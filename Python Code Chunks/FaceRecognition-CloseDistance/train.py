import os
import face_recognition
import pickle
import cv2
from sklearn.svm import SVC
import sys



def trainEncode():
    # f = open ("encodenewblah2.dat","rb")
    f=open("encodingsVideo.dat","rb")
    print("training SVM linear %s") #train SVM
    encoding,label=pickle.load(f)
    clf.fit(encoding, label)
    f.close()
    f=open("Model-CloseDistVid.dat","wb")
    s = pickle.dump(clf,f)
    f.close()



# imgFolder=str(sys.argv[1])
#
# folderList = os.listdir(imgFolder)
imgs = []
s_image = []
s_face_encodings = []
label = []
clf = SVC(kernel='rbf', probability=True, tol=1e-3,C=10)
# print (folderList)
trainEncode()
