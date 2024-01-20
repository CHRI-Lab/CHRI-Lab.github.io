---
title: Demo 1 OpenCV Basics 
summary: Show first Opencv commands
tags:
- opencv
date: "2020-01-01T00:00:00Z"

weight: 1

header:
  caption: ""
  image: ""

links:
  - icon_pack: fab
    icon: medium
    name: JupyterNotebook
    url: '/img/teaching/computer_vision/week1/W1_Demo1_Image_Formation_OpenCVBasics.ipynb'

type: book
---




```python
import numpy as np 
import cv2
import matplotlib.pyplot as plt
```


```python
# read an image
img = cv2.imread('test1.jpg',1)
```


```python
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


```python
# print image dimension
print(img.shape)
```

    (225, 225, 3)
    


```python
# print a pixel value
px = img[100,100]
print(px)
```

    [  8 150 255]
    


```python
# get an ROI region
roi = img[100:120, 100:120]
# replace another region in the image with the selected ROI
img[180:200, 180:200] = roi
```


```python
# display the modified image
cv2.imshow('image2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


```python
# write the image output into a new file
cv2.imwrite('res_1.png',img)
```




    True




```python
plt.imshow(img)
```




    <matplotlib.image.AxesImage at 0x28e7f6ba550>




![png](/img/teaching/computer_vision/week1/demo1/output_9_1.png)



```python
#convert BGR to RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
```




    <matplotlib.image.AxesImage at 0x28e7f7680b8>




![png](/img/teaching/computer_vision/week1/demo1/output_10_1.png)



```python
## to look at the documentation of a function inside your notebook use a '?'
cv2.cvtColor?
```

    cvtColor(src, code[, dst[, dstCn]]) -> dst
    .   @brief Converts an image from one color space to another.
    .   
    .   The function converts an input image from one color space to another. In case of a transformation
    .   to-from RGB color space, the order of the channels should be specified explicitly (RGB or BGR). Note
    .   that the default color format in OpenCV is often referred to as RGB but it is actually BGR (the
    .   bytes are reversed). So the first byte in a standard (24-bit) color image will be an 8-bit Blue
    .   component, the second byte will be Green, and the third byte will be Red. The fourth, fifth, and
    .   sixth bytes would then be the second pixel (Blue, then Green, then Red), and so on.
    .   
    .   The conventional ranges for R, G, and B channel values are:
    .   -   0 to 255 for CV_8U images
    .   -   0 to 65535 for CV_16U images
    .   -   0 to 1 for CV_32F images
    .   
    .   In case of linear transformations, the range does not matter. But in case of a non-linear
    .   transformation, an input RGB image should be normalized to the proper value range to get the correct
    .   results, for example, for RGB \f$\rightarrow\f$ L\*u\*v\* transformation. For example, if you have a
    .   32-bit floating-point image directly converted from an 8-bit image without any scaling, then it will
    .   have the 0..255 value range instead of 0..1 assumed by the function. So, before calling #cvtColor ,
    .   you need first to scale the image down:
    .   @code
    .   img *= 1./255;
    .   cvtColor(img, img, COLOR_BGR2Luv);
    .   @endcode
    .   If you use #cvtColor with 8-bit images, the conversion will have some information lost. For many
    .   applications, this will not be noticeable but it is recommended to use 32-bit images in applications
    .   that need the full range of colors or that convert an image before an operation and then convert
    .   back.
    .   
    .   If conversion adds the alpha channel, its value will set to the maximum of corresponding channel
    .   range: 255 for CV_8U, 65535 for CV_16U, 1 for CV_32F.
    .   
    .   @param src input image: 8-bit unsigned, 16-bit unsigned ( CV_16UC... ), or single-precision
    .   floating-point.
    .   @param dst output image of the same size and depth as src.
    .   @param code color space conversion code (see #ColorConversionCodes).
    .   @param dstCn number of channels in the destination image; if the parameter is 0, the number of the
    .   channels is derived automatically from src and code.
    .   
    .   @see @ref imgproc_color_conversions
    
    



```python

```
