>>> import numpy as np
>>> import cv2

# "1" indicates to use the default colors and channels
# Passing "0" instead will read the image as Black and White.
>>> img = cv2.imread("opencv-logo.png", 1)


>>> img 
# It yields the Pixel Values as shown here.
array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ..., 
       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)


>>> type(img)
<class 'numpy.ndarray'>


>>> len(img)
739    # It refers to the number of rows in ths current Image


>>> len(img[0])
600    # It refers to the Columns in the current Image


>>> len(img[0][0])
3       # Number of Channels
        # If there is a Transparency Layer or an Alpha Layer in the Image , It shows 4.


>>> img.shape
(739, 600, 3) # (rows,columns,channels)


>>> img.dtype
dtype('uint8') # Abbreviated as Unsigned Integer Value of 8


>>> 2**8
256            # Range of values vary from 0 to 255 (total 256)


>>> img[10, 5] # We can access the pixel values of the Image. say 10th Row, 5th Column.
array([255, 255, 255], dtype=uint8)


>>> img[:, :, 0] # Single Channel Image
array([[255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       ..., 
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)


>>> img.size # Total Number of pixels in this Image.
1330200