import numpy as np
import cv2

color = cv2.imread("butterfly.jpg",1)

# Converting 3 channel image to 1 channel and Saving the gray Image
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg",gray)

# Adding an Additional Channel to already Loaded Image

# For creating the other channel Let us grab the Individual channels from our Color Image

# Instead of Split We can do in this way too.
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

# We can reuse our channels to create the 4th Channel which acts as Transparency Layer

# If for example, We want to make the Non Green Parts of the Image Transparent we could pass the g cahnnel as 4th Layer
# Where a High Value or a very green pixel will show as a high Aplha Layer (Not Transparent)

rgba = cv2.merge((b,g,r,g))

# jpg images dont support Image Transparency so we are using png.
cv2.imwrite("rgba.png",rgba)
