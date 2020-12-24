                                            
                                            # Overview of Face and Features Detection 

# This chapter is dedicated to feature recognition and face detection. A feature is any part of an image which can be used to understand an image better and to help perform a needed task. Features can be visual components of an image or more mathematical properties of the patterns and arrangement of the pixel values.

# Good features are invariant to changes like lighting or scaling. For example, the circularity of a segmented object or the ratio of the shortest to the longest axis. Statistical properties of an image or color distribution could also act as features if it fits the problem. 

# Features are identified by classifiers to either detect or recognize objects in an image. Note to be careful how you use the term detection versus recognition. Detection is often the step prior to recognition. 

# For example, with faces, you first might detect whether a face exists in an image, and a follow-up step might be to understand if that face matches any image in a database. In this case, features such as the distance between eyes in an image may be used both for the detection process to see whether or not a face actually exists, but also used as a classifier for the recognition process to see which face it specifically matches with. 

# In this chapter, we will be looking at two specific algorithms, template matching for general object recognition, and hard cascading as a means for face detection.


                                            # Introduction to template matching


 # When it comes to feature detection, template matching is a readily available and straightforward method. The way template matching works, is it searches for a similar pattern between two images. This is accomplished by taking a reference image, called a template and sliding it around the other comparison image, taking a difference at every position. 
 
 # The result, is a black and white gray scale image with varying intensities showing how well it matched at each position. 
 
 #  Typically, template matching is actually applied in a two-dimensional format but the concept is the same as 1D, your source template image will scroll horizontally and vertically across the entire image, taking a difference at each location. 
 
 # The sum result of that difference is put into the pixel value, where a zero sum difference mean the exact same images becomes white and a perfect difference become black. Typically you'll find there's lots of gray in your image as there are always going to be partial matches of some of the pixels in the template versus your image. 
 
 # Typically with template matching you don't actually use an element from the source image yourself but something that is predetermined, such as a face or a known generic object that is expected to be found in the scene.
 
 # Given that, it's important to understand a few of the limitations of template matching. If your template is scaled compared to your Source image then it will not work very well, likewise if your template is rotated and the template looks different at those different rotations, it may reduce the effectiveness of the template matching. Despite that it's still a very efficient algorithm and can be very useful in some scenarios.

 
import numpy as np
import cv2


# Now we can dive into template matching as a means to detect features in an image. Template matching works by sliding a source template image and making a difference at every possible location against a reference image. This difference shows us how close those two images are together and if there are any close matches between the template and the source frame it will indicate that area as a very bright spot in the resulting image.

template = cv2.imread('template.jpg',0)
frame = cv2.imread("players.jpg",0)

cv2.imshow("Frame",frame)
cv2.imshow("Template",template)

# Running Template Matching
result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

# Now we're going to try and draw that location by getting the maximum brightness out of the result image.

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val,max_loc)
cv2.circle(result,max_loc, 15,255,2)
cv2.imshow("Matching",result)

cv2.waitKey(0)
cv2.destroyAllWindows()