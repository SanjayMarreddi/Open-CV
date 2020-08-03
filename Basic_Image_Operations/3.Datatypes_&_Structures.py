import numpy as np
import cv2

# In an Image Pixels values 0 refers to Pure Black and 255 refers to Pure White

# First We specify size of Image to be generated and 
# followed by type so that it will give range of Pixel values to be used inside the Image
black = np.zeros([150,200,1],'uint8')

# In imshow First variable is name of WINDOW and next one is name of IMAGE
cv2.imshow("Black",black)
print(black[0,0,:])

ones = np.ones([150,200,3],'uint8')
cv2.imshow("Ones",ones)
print(ones[0,0,:])

white = np.ones([150,200,3],'uint16')
white *= (2**16-1) # It creates the Full White Image
cv2.imshow("White",white)
print(white[0,0,:])

color = ones.copy() # .copy() creates the Deep Copy of ones Matrix
color[:,:] = (255,0,0) # It is having BGR format.
cv2.imshow("Blue",color)
print(color[0,0,:])


cv2.waitKey(0)
cv2.destroyAllWindows()
# This will make sure that the user Interface will hang until We have taken a look at the Image before closing all the Windows
