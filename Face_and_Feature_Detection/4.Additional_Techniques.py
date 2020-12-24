
# From a computer vision standpoint, we have only scratched the surface with the topics covered so far. Let's take a moment to briefly look at some other algorithms in the field. One of those applications we've already seen briefly under the hood is machine learning. Specifically, we have been looking at supervised machine learning. 

# This is a form of machine-based learning where you train a classifier using already-tagged or identified data. For example, you start a pool of images that is an apple and then a pool of images which are not an apple. The classifier then builds little tests, extracting features from the image. And for each of those tests, it is evaluated of how well it indicates it being one image object or another. When it comes to supervised machine learning, an important concept is the confusion matrix. 

# The idea is that you can evaluate the effectiveness of your classifier or machine learning data by testing it against a set of images that were not used in the training process. Here you can see that the true positives are the diagonals and the false positives are all the other areas such as when a key is accidentally recognized as an apple. Another area of computer vision is text recognition. 

# I'm sure you could imagine countless applications for the usefulness of OCR text recognition. But to name a few explicitly, you can imagine enabling autonomous vehicles to read signs or being able to help auto-sort and process letters with handwritten addresses. 

#  It has a general process of identifying if text is present in an image such as looking for areas of high contrast or certain identified shapes, and then it will often segment and warp and then run a machine-learned process to extract features and do character recognition.

#  Then, there could be further processing done to detect groupings of words, lines, or sentences, and so forth. Another field is optical flow and object tracking as well as scene reconstruction. Optical flow is a key algorithm and technique for real time applications as well as for other applications that are used to reconstruct a scene.
 
#  The idea is to calculate and understand the apparent motion within a scene and for all the objects present in an image. This is done by evaluating the change of pixels over time and between frames. When it comes to object tracking, it is typically faster to track an object between frames than it is to detect an object between frames.

#  For example, with face tracking, it may take some computational energy to detect whether or not a face is in the scene. But once you have found a face and you know a little bit about what that particular face looks like, it becomes easier to track it than it would be to detect that face on every frame of a video.

#  Yet another niche but good example of the use case of computer vision technology is the reading and creating of QR codes or scanners in general. We can see here a typical flowchart for the QR reading algorithm.

#  You might notice this pattern of starting with detection, then segmentation and transformation to put the image in a more consumable format. Detection could be done using something such as a gradient frequency or edge detection map to filter a range of patterns. 

#  Then, the QR code is corner-pin warped into a more parallel format where it then becomes easy to read off the individual bits of the QR code by reading the black versus white areas in a serial manner. Then, using an understanding of the format and structure of a QR code, the information is converted and extracted from the image.
 
#  When it comes to generating a QR code, it's essentially the same process but in reverse. QR codes even have the ability to have built-in error or bit checking to help identify when a wrong character was detected due to, for example, bad segmentation or uneven lighting. 

# Again, this is only a short sampling of the possibilities of this library, and new techniques are always being developed. For more use cases and resources, take a look at opencv.org.


# There was a lot to cover, and there are still plenty of areas to look into. If you want to become more familiar with image processing, I recommend looking into other algorithms and techniques available with the OpenCV library and to become familiar with the OpenCV documentation. Note that the library isn't limited to just Python.

#  The same algorithms and methodology we learned here will work with OpenCV for iOS and Android as it would for compiled C++ code. If you find yourself searching for more online resources, such as blogs or tutorials, be mindful that many demonstrate the use of older Python 2 releases or earlier OpenCV builds.

#  Generally speaking, though, the techniques and commands remain consistent across versions of OpenCV and Python. If you want to learn more about myself and my own past experience with OpenCV, my name is Patrick Crawford, and my website is theduckcow.com. I'm also on Twitter @TheDuckCow. Thanks again for taking this course, and I wish you the best of luck with all of your image processing endeavors.