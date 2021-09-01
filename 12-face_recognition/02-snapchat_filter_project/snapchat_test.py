import cv2
import numpy as np

img = cv2.imread('Before.png')
eyes_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#nose_detector = cv2.CascadeClassifier('Nose18x15.xml')

#ret,frame = img.read()
#gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#if ret == False :
#	continue


cv2.imshow('Tyrion', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
