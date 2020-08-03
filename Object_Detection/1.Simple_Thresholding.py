# Now we are focused on extracting features and objects from images. An object is the focus of our processing. It's the thing that we actually want to get, to do further work. In order to get the object out of an image, we need to go through a process called segmentation. 

# Segmentation can be done through a variety of different ways but the typical output is a binary image. A binary image is something that has values of zero or one. Essentially, a one indicates the piece of the image that we want to use and a zero is everything else. 

# Binary images are a key component of many image processing algorithms. These are pure, non alias black and white images, the results of extracting out only what you need. They act as a mask for the area of the sourced image. After creating a binary image from the source, you do a lot when it comes to image processing. 

# One of the typical ways to get a binary image, is to use what's called the thresholding algorithm. This is a type of segmentation that does a look at the values of the sourced image and a comparison against one's central value to decide whether a single pixel or group of pixels should have values zero or one.


import numpy as np
import cv2

# "0" tells opencv to load the GRAY IMAGE
bw = cv2.imread('detect_blob.png', 0)
height, width = bw.shape[0:2]
cv2.imshow("Original BW",bw)

# Now the goal is to ample a straightforward thresholding method to extract the objects from an image. We can do that by assigning all the objects a value of 1 and everything else a value of 0.

binary = np.zeros([height,width,1],'uint8') # One channel binary Image

thresh = 85	# Every pixel is compared against this

for row in range(0,height):
	for col in range(0, width):
		if bw[row][col]>thresh:
			binary[row][col]=255	#  I just said that a binary image is consisting of either 0s or 1s, but in this case we want to display the image in the user interface, and because of OpenCV's GUI requirements, we want to actually show a 255 or 0 value-based image. That way, the binary image will appear white where we actually want our objects.

cv2.imshow("Slow Binary",binary) # Slower method due to two for Loops

# Faster Method using OPENCV builtins.
# Refer Documentation to explore More

ret, thresh = cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)
cv2.imshow("CV Threshold",thresh)

# This is a Simple example of IMAGE SEGMENTATION using Thresholding !

cv2.waitKey(0)
cv2.destroyAllWindows()