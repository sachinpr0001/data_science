import cv2

img = cv2.imread("logo.jpg")
gray = cv2.imread('logo.jpg',cv2.IMREAD_GRAYSCALE)


cv2.imshow('image',img)
cv2.imshow('gray',gray)
#Wait for any key before image disappears
cv2.waitKey(0)
cv2.destroyAllWindows()