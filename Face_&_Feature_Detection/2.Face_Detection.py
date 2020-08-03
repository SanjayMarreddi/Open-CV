# Before we jump into creating stable face detection, let's take a moment to understand a Haar cascade classifiers, a form of future-based machine learning.

# It works by first training a classifier with set of labeled positive and negatives. Or in other words, indicating to the classifier that these are sets of images that have faces and these are sets of images that don't have faces. 

# This classifier then learns from the set by understanding and extracting features from all the images. For example, it may naturally learn that the region of the eye is as typically darker than the region of the cheeks below and may use that as one of its thousands of indicators that help understand whether not a particular region of interest, or ROI, is a face or not. 

# After the training is completed, and a classifier is defined, we use the classifier in a cascaded manner to run through all the feature checks. This cascade method works like a waterfall, where you apply the fastest and most general checks first in order to quickly rule out areas that are definitely not matching a face without spending too much computational time. 

# As it becomes more refined and goes through more classifiers, it gets more and more sure that the region of interest is actually a face. If it gets through all the cascaded classifiers, it is then marked as a valid face and outputs the bounding blocks. 

# When we run the face detection algorithm and open CV, using the training data, we essentially leverage the already trained information into a cascade classifier which would then output the set of found faces and the regions of interests. Note however, is not always perfect.

#  And is possible that there will still be false positives and false negatives. Since your training data is rarely ever exactly the same as the applied data, you always are at risk at false negatives or positives. But there are parameters to tweak the classifier to make it more accurate for the particular situation.

import numpy as np
import cv2


# Now, let's take a look at the specific use case of detecting faces in image using the pre-learn hard classifier. Again, note that detection is not the same thing as recognition; we are only detecting if and where faces are located in an image.

img = cv2.imread("faces.jpeg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
path = "haarcascade_frontalface_default.xml"

# Creating Cascade Classifier Object. This actually loads in the xml and initializes our cascades of function and classifiers. 
face_cascade = cv2.CascadeClassifier(path)

# The first one will be scaleFactor equals 1.10 and noting that this is a compensating factor for only wanting faces close to the camera

# minNeighbors, This factor sets a number of nearby object detections required before it's considered a face

#Th en, in this last factor, is the actual minimum size of a face to count before it's detected and in your last parenthesis

# We note that the result of this operation is creating a list that contains all the bounding boxes for detected faces. If there are no faces found in an image, the length of a list would be set as zero

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
print(len(faces))


# Drawing the Bounding Boxes onto Original Image
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
	# 2nd Parameter indicates TOP LEFT CORNER
	# 3rd Parameter indicates BOTTOM RIGHT CORNER
	# 4th Parameter indicates COLOR of BOX
	# 5th Parameter indicates Line Thickness

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# You can typically (mumbles) the classifier used to improve your results or you can train your own data.