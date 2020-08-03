# Often we need to pre-process images in order to improve our final result, and in the case of extracting contours from individual objects in an image it is often handy to first detect and accentuate the edges within an image.

# Canny Edges is one type of edge detection algorithm that works quite well to help create better separation of objects within the image. Generally speaking, edge detection algorithms look at the rate or speed at which color changes across the image. 

# Canny Edges is a specific form of that algorithm that creates a single pixel wide line at key high gradient areas in the image. This can help break up the object if there was an overlap in our segmentation process.

#  Let's take a look at how we can use Canny Edges. Imagine the goal here is to try and segment out each individual tomato. If we're running a threshold, we may run into an issue where the different tomatoes get blobbed together as one single object.

import numpy as np
import cv2

img = cv2.imread("tomatoes.jpg",1)

# Conversion
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Thresholding
res,thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV) #  Essentially this line of code is saying that we want to extract all of the pixels that have a hue of value 25 or less as We have INV
cv2.imshow("Thresh",thresh)

# There's two threshold values we want to give. We can play with these values if we want, but for this purpose, let's just type in 100 and 70 for the lower and upper limit of the threshold of the edges
edges = cv2.Canny(img, 100, 70) 
cv2.imshow("Canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()