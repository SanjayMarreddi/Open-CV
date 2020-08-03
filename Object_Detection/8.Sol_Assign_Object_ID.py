import numpy as np
import cv2
import random # To help in drawing with Random Colors

img = cv2.imread("fuzzy.png",1)
cv2.imshow("Original",img)

# Convert to Gray so that we can do Thresholding
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Next, this little trick will actually help make our adaptive thresholding work better if we use a blur. 
blur = cv2.GaussianBlur(gray, (3,3),0)

# Note that we are selecting the inverse in this case because the foreground of the image was white and we want to take out the objects which are going to be darker than this color therefore we're inversing the threshold.
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
cv2.imshow("Binary",thresh) 


# Now lets add Contours.
_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours)) # To know how many objects are recognized

# According to the task here, we want to make sure that we only draw the largest contours, so to do this we actually want to run some filtering on our contours.
filtered = []
for c in contours:
	if cv2.contourArea(c) < 1000:
		continue
	filtered.append(c)

print(len(filtered))

# Drawing the Contours
objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')
for c in filtered:
	col = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) 
	cv2.drawContours(objects,[c], -1, col, -1) # Drawing each contour.
	area = cv2.contourArea(c)
	p = cv2.arcLength(c,True)
	print(area,p)

cv2.imshow("Contours",objects)
	

cv2.waitKey(0)
cv2.destroyAllWindows()

# In the middle of the large green square on the right, there appears to be another smaller contour that was drawn within. Essentially there was actually a unique object that open CV found and drew on its own and it happened to be larger than our threshold. 

# For reasons like this you will often find that people will actually run contours twice. The first time it will merge overlapping contours and then the second time there'll be whole, incomplete objects.