import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("Image",color)
# When cv2 runs the Script , It will place the Window in the Top Left Hand Corner as we specified (0,0).
cv2.moveWindow("Image",0,0)
print(color.shape)
height,width,channels = color.shape

# It will split our channels of the color Image into each of its Components as an Individual Matrix
b,g,r = cv2.split(color)

# empty command will create an uninitialized array Matrix. This is the fastest way to create a Matrix but it will have NON SET values.
rgb_split = np.empty([height,width*3,3],'uint8')

rgb_split[:, 0:width] = cv2.merge([b,b,b]) # This will place our Blue Channel fully on the Left Hand Side of our Image.
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)


# Now Let us look at another Color Space called Hue Saturation and Value Space.
# HUE Channel  indicates the Type of Color that we see in a 360 Degree Format
# Saturation Channel has an indication of how saturated an Individual color is
# VALUE Channel indicates how Luminous the Channel is.


# We are doing a Conversion from BGR format to HSV 
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
# axis =1 indicates to concatenate so that Images appear Side by Side
hsv_split = np.concatenate((h,s,v),axis=1)
cv2.imshow("Split HSV",hsv_split)

cv2.waitKey(0) # "0" tells the Interface to Hold
cv2.destroyAllWindows()