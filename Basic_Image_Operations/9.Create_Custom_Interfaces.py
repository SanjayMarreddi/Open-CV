# Now, We're going to draw a circle onto the screen and we're going to place the circle based on wherever we have last clicked

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Let us initialize some Variables
# Note that 255 is assuming, as is typical, that the webcam has an unsigned integer eight depth.

color = (0,255,0)   # Green (BGR)
line_width = 3		# Note that if we gave a value of "-1" it would mean that the circle would be filled instead of having a line thickness. 
radius = 100
point = (0,0)

# Essentially this is a callback that will run every time that you click the mouse on the video feed and allows us to process some information
def click(event, x, y, flags, param):
	global point, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		print("Pressed",x,y)
		point = (x,y)


# Note that we can also capture other events such as event r button down, event l button up or even event underscore mouse move.
# The final step is to register this click with the open cv handler.
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)

while(True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.circle(frame, point, radius, color, line_width)
	cv2.imshow("Frame",frame)

	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()