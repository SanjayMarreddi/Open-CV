# While simple thresholding is a powerful algorithm, it has its limits, such as when there's uneven lighting in an image. This is where adaptive thresholding comes to the rescue. This is a technique that can increase the versatility of image thresholding operations. 

# Instead of taking a simple global value as a threshold comparison, adaptive thresholding will look in its local neighborhood of the image to determine whether a relative threshold is met. In this way, it is possible to counteract issues, such as uneven lighting

import numpy as np
import cv2

img = cv2.imread('sudoku.png',0) # Gray Image :You'll find this is very customary that we only work with black and white images when doing segmentation
cv2.imshow("Original",img)

# Basic Thresholding
ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("Basic Binary",thresh_basic)

# Adaptive Thresholding
thres_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive Threshold",thres_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()