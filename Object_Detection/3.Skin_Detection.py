# With an understanding of the different thresholding types, we can apply the use case of detecting and segmenting the skin tones from an image.

# This will also cover the use of composite filtering to improve the result if no single threshold will work on its own. 

# We would find that no single threshold or adapted threshold would do the job on its own. Therefore, we need to combine multiple together in this Case


import numpy as np
import cv2

img = cv2.imread('faces.jpeg',1)

# Conver into HSV format
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split HSV",hsv_split)


# Basic Threshold(Quick Filtering) in SATURATION CHANNEL
ret, min_sat = cv2.threshold(s,40,255, cv2.THRESH_BINARY)
cv2.imshow("Sat Filter",min_sat)


# Basic Threshold(Quick Filtering) in HUE CHANNEL
# Note that this indicates that we're going to do the inverse of the normal order of the threshold. In this case, this will make values zero to 15 white, and everything else black.
ret, max_hue = cv2.threshold(h,15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter",max_hue)

# Combining the Filters
final = cv2.bitwise_and(min_sat,max_hue)
cv2.imshow("Final",final)
cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#  On a closing note, it's important to acknowledge that this is not necessarily the most robust method to detect faces. More advanced techniques would use machine learning, or would use light invariate methods. 

# In this case, we're using simple hardcoded value thresholds that may not work in all environments. To get your own results, or with better results on other images, you may have to tweak these parameters