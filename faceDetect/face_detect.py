""" A script to detect faces in image
using OpenCV Haarcascades.

Author: Nahom Abi

Date: 05/16/2017

"""

import cv2

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
image = cv2.imread('faceu_20170918213700.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.17,
    minNeighbors=5,
    minSize=(30,30)
)

print("{} faces detected.".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Faces', image)
cv2.imwrite('detected2.jpg', image)

cv2.waitKey(0)
