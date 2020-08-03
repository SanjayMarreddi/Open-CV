# Once We have segmented out the key areas of an image, the next step is typically to identify the individual objects.

# One powerful way is to use OpenCV's implementation of contours. The goal of contours is to take a binary image and create a tightly fitting closed perimeter around all individual objects in the scene. Each perimeter is called a contour.

# From a mathematical point of view, it is called an iterative energy reduction algorithm. But conceptually, we can think of it as an elastic film that starts on the edges of an image and squeezes in around all the objects and shapes. It creates the boundary around all these objects. 
 
# One thing to be aware of is the idea of neighborhoods and connectedness. Contours will consider any pixel value above zero as part of the foreground, and any other pixels touching or connected to this pixel will be made to be part of the same object.

# As the algorithm runs, it tries to reduce the energy or the bounding box around all these objects until it comes to a converged result. It's important to understand that while this may be an iterative algorithm, we know contours will always converge, so it'll never be stuck in an infinite loop. 

# At the end, you have a list of contours, and each contour is simply a linear list of points which describe the perimeter of a single object. They are always enclosed, a technical term meaning there are no gaps. This means they can be safely drawn back onto an image and completely filled with a new color.

#  Contours is one of the gateways to determine many other useful properties about a single object within an image, making it a very powerful algorithm at our image processing disposal. It moves from the step of object segmentation, often done by thresholding, into the step of object detection.

import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)
# Converting to GRAY
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)

# It actually Outputs 3 Values . We wont use 1st one. Followed by contours, which is the actually list of individual contours and recall that each contour is a list of points which describe a parameter of an object.

#  Followed by hierarchy. Hierarchy is, essentially, a parent-child relationship of all the contours. A child, for example, would be if one contour is enclosed by another
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy() # Make a Deep Copy of Original IMAGE
index = -1         # This'll be the index of the contour we want to draw and in this case, using an index value of minus one, we'll draw all the contours.
thickness = 4 
color = (255, 0, 255) # Color of Contours being drawn : Here PINK

cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow("Contours",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# A common secondary step after running contour is to filter through and only look at a contour you need to use. To do this, it's often useful to look at various parameters and information that you can get from a single contour. Nonetheless, we can already see that contours is a very easy-to-use and powerful algorithm in open OpenCV.