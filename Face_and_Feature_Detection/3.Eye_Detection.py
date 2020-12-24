# Let's complete this chapter with a challenge. Specifically, let's try and find all the eyes in an image and place circles around them. To do this, leverage a haarcascade method similar to how we detected faces in the previous module.

# This time, use the provided haarcascade_eye.xml file, which has specifically been pre-trained for detecting eyes in an image. Additionally, try to reduce the number of false positives and false negatives as much as possible. 

# In this scenario, a false positive is drawing a circle where there's not an eye, and a false negative is not drawing a circle where there is an eye

import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "haarcascade_eye.xml"

eye_cascade = cv2.CascadeClassifier(path)

eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.02,minNeighbors=20,minSize=(10,10))
print(len(eyes))

# We always get the Info to draw a Rectangle
for (x, y, w, h) in eyes:
	xc = (x + x+w)/2
	yc = (y + y+h)/2
	radius = w/2 # or h/2
	cv2.circle(img, (int(xc),int(yc)), int(radius), (255,0,0), 2)
cv2.imshow("Eyes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# A lot of time can be spent adjusting the parameters.
# Note as it was true with the face detection, it all comes down to the fact that this is machine learned data, in other words your results are only as good as your training data and if the training images were vastly different from the images we're using now, you may end up being required to create your own classifier and training data.