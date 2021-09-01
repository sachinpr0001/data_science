# Simple program to read and show an image

import cv2

img = cv2.imread('logo.jpg')
gray = cv2.imread('logo.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Mountain', img)
cv2.imshow('Gray Mountain', gray)

cv2.waitKey(0) # Program will stop when any key is pressed
cv2.destroyAllWindows()