import numpy as np
import cv2

# Reading the image using its path
img = cv2.imread("opencv-logo.png")

# Displaying the image after creating a Window named "Image", 
# Here we are using the default Window Behaviour
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)

# It tells our interface to wait for particular no of seconds once the img is displayed and gets closed automatically
# waitKey Function will capture the key pressed   on the Keyboard. Esc has a value of 27
cv2.waitKey(0)

# Saving this image as per our requirement , 
# We can change extension also . Moreover the images encoding is also changed by OpenCv Environment.
cv2.imwrite("output.jpg",img)
