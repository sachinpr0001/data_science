import cv2
import numpy as np
import os


img1 = cv2.imread('/Test/Before.png')
img2 = cv2.imread('/Test/mustache.png')
img3 = cv2.imread('/Test/glasses.png')

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

nose_cascade = cv2.CascadeClassifier("./Train/third-party/Nose18x15.xml")

img=cv2.imread(“Train/glasses.png”,cv2.IMREAD_UNCHANGED)
print(img.shape)


















"""
########## KNN CODE ############
def distance(v1, v2):
	# Eucledian 
	return np.sqrt(((v1-v2)**2).sum())

def knn(train, test, k=5):
	dist = []
	
	for i in range(train.shape[0]):
		# Get the vector and label
		ix = train[i, :-1]
		iy = train[i, -1]
		# Compute the distance from test point
		d = distance(test, ix)
		dist.append([d, iy])
	# Sort based on distance and get top k
	dk = sorted(dist, key=lambda x: x[0])[:k]
	# Retrieve only the labels
	labels = np.array(dk)[:, -1]
	
	# Get frequencies of each label
	output = np.unique(labels, return_counts=True)
	# Find max frequency and corresponding label
	index = np.argmax(output[1])
	return output[0][index]
################################

"""
