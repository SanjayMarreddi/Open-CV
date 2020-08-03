# OpenCV provides easy access to video feeds, enabling applications to provide real-time processing & even display the processed video output. 
# In a real-time application, the video feed is tapped for an image at the start of a repeating loop which represents the actual image processing to occur.

import numpy as np
import cv2

# Next we're going to capture or request from the operating system to use the camera. We're going to specify a zero argument input that indicates continuous
cap = cv2.VideoCapture(0)

# Now we're going to create a while loop which will be our actual loop of the video feed. 
while(True):
	
	# This read command will always read a new frame from the video capture
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.imshow("Frame",frame)

	# The main thing should make sure is to register a wait key, because if we don't register a legitimate exit to our loop, 
	# then we may end up getting stuck and have to force quit the application

	# This will indicate that it'll run every one millisecond.If you were to pass a value of 10, it would wait 10 milliseconds before the 
	# next loop and so forth

	ch = cv2.waitKey(1)
	# ch is the actual key that we have captured. So, if we want to take a look and break the loop given a certain letter has been pressed, 
	# for example, we could type if ch and 0xFF as shown 
	if ch & 0xFF == ord('q'):
		break


#And then finally, it's important that we use cap.release at the very end of the program.
cap.release()
cv2.destroyAllWindows()