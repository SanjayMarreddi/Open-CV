# In this chapter, we reviewed a few ways to approach segmenting out objects in an image and detecting properties of those objects. A few areas we looked at included both simple and adaptive thresholding using edges to help break down apart closely fitting objects.

#  We also briefly looked at how to composite multiple thresholds of different types together, and in the last chapter, we saw how to use Gaussian blurs to reduce noise, and dilation and erosion filters to reduce small speckles or gaps. 

# These are just some of the image processing tools helpful in segmenting out objects. It's important to keep in mind the context. Know what the application will be used for, and develop segmentation that will fit the use case. 

# Do you know that your lighting will always stay roughly the same for different image inputs? If so, it may be more effective to use non-adaptive thresholding; perhaps you can improve your thresholding by gathering your own global average or mean.

#  How about object orientation and scale? Can you make assumptions about the size of an object in an image, therefore allowing you to filter out anything that doesn't fit that size? Furthermore, is it a real-time application, where consistency between frames might be very important? As for filtering, is it a problem to over filter or under filter the results?

#  For example, if detecting an object triggers an action, such as sending email, then perhaps you want to be more sensitive about not having false positives. Though this course only covers a few basic ways to identify and characterize image objects, there are many other applications and advanced techniques to segment out objects in an image or sequence. 
 
# We touched upon a priori means of object detection. This means having some prior knowledge about the context or inputs ahead of time. For example, if you know that the subjects of your image will always be against a black background, it allows you to make different assumptions and processing technique decisions that wouldn't hold up in more general situations.

#  When looking to detect and segment out objects in an image, be aware of all the tools at your disposal. Know how the parameters of the situation will vary, and think about how you can break the process down into smaller steps.


# CHALLENGE
# let's take this fuzzy image and segment out the objects and then redraw them onto a new image with unique colors. The specific goals are to only draw large objects which have an area of larger than 1,000 square pixels. Additionally, each object needs to have its own color. 

import numpy as np
import cv2

img = cv2.imread("fuzzy.png",1)


cv2.waitKey(0)
cv2.destroyAllWindows()

