import numpy as np
import cv2

image = cv2.imread("thresh.jpg")
cv2.imshow("Original",image)


# Now we will take a look at a few useful filtering functions often used to pre-process or adjust an image prior to doing more complex operations
 
# These operations help reduce noise or unwanted variances of an image or threshold. The goal is to make the image easier to work with.

#  The three filters are the Gaussian Blur, Erosion, and Dilation filters. 

# The Gaussian Blur filter smooths an image by averaging pixel values with its neighbors. It's called a Gaussian Blur because the average has a Gaussian falloff effect. 

# In other words, pixels that are closer to the target pixel have a higher impact with the average than pixels that are far away. 

# This is how the smoothing works. It is often used as a decent way to smooth out noise in an image as a precursor to other processing.


# (5,55) indicates how much to blur the image on x and y axis respectively. They should be ODD values always 
blur = cv2.GaussianBlur(image, (5,55),0)
cv2.imshow("Blur",blur)

# Now we'll take a look at the Dilation and Erosion filter. There are two operations that look to expand or contract the foreground pixels
# of an image to help remove or accentuate small pixel details, such as speckles. 

# They work by sliding a kernel template, a small square, across an image. As you can see, the Dilation effect works to turn black pixels, 
# or background pixels, into white pixels, while an erosion filter looks to turn white pixels into black pixels, essentially eating away at
# the foreground.

# The small structuring element that was moved across the image is called the kernel and defines where and how to mark a pixel changed by that filter

# Here also they should be ODD values
kernel = np.ones((5,5),'uint8')

dilate = cv2.dilate(image,kernel,iterations=1)
erode = cv2.erode(image,kernel,iterations=1)
# To increase the effect of these filters we can increase no of Iterations

cv2.imshow("Dilate",dilate)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()