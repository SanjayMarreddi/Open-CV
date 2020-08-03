import numpy as np
import cv2

img = cv2.imread("players.jpg",1)

# Scale : cv2.resize is the Main Resizing Function.

# After passing the img , We usually pass the Absolute Size in Pixels.
# Here we specifed (0,0) to not set an absolute size in pixels and we can pass optionally in our relative factors fx,fy
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Now we are explicitly resizing to (600,600)
img_stretch = cv2.resize(img, (600,600))

# Instead of using the default interpolation mode during Scaling We are using  INTER_NEAREST.
img_stretch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half",img_half)
cv2.imshow("Stretch",img_stretch)
cv2.imshow("Stretch near",img_stretch_near)

# Rotation :  The way we're going to rotate an image is by applying a matrix transformation.
 
# First We specify the point about which Rotation is to be performed. (0,0) indicates the TOP LEFT hand corner followed by angle in degrees.

M = cv2.getRotationMatrix2D((0,0), -30, 1)

# You can now use this transformation matrix to actually rotate an image by typing below line:-

rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Rotated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()