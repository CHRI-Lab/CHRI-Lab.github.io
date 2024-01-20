---
title: Demo 2 Color Spaces 
summary: Converting and displaying different colorspace channels in opencv
tags:
- opencv
date: "2020-01-01T00:00:00Z"
    
weight: 2 
header:
  caption: ""
  image: "teaching/computer_vision/week1/demo2/beachBox.jpg"

type: book

---




```python
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("beachBox.jpg")
print(img.shape)
plt.axis('off') # if you want to hide the axis
plt.imshow(img)
plt.show()
```

    (743, 1280, 3)
    

![png](/img/teaching/computer_vision/week1/demo2/output_1_1.png)


Documentation on [imread](https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56) 

Bookmark this [https://docs.opencv.org/](https://docs.opencv.org/)




```python
cv2.__version__
```




    '3.4.5'



# Plot the image


```python
RGB_im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(RGB_im.shape)
plt.imshow(RGB_im)
plt.show()
```

    (743, 1280, 3)
    


![png](/img/teaching/computer_vision/week1/demo2/output_5_1.png)


# RGB Channel Decomposition

![](/img/teaching/computer_vision/week1/ColorSpaces/RGB.jpg)


```python
b = RGB_im.copy()
# (x,y,nb_channels = 3  [R, G, B])
# set green and red channels to 0
b[:, :, 0] = 0 # sets the value in the red channels to 0
b[:, :, 1] = 0 # sets the value in the green channels to 0


g = RGB_im.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = RGB_im.copy()
# set blue and green channels to 0
r[:, :, 2] = 0
r[:, :, 1] = 0

rg =  cv2.cvtColor(r,cv2.COLOR_RGB2GRAY)
bg =  cv2.cvtColor(b,cv2.COLOR_RGB2GRAY)
gg =  cv2.cvtColor(g,cv2.COLOR_RGB2GRAY)

plt.imshow(RGB_im)
plt.show()
plt.imshow(r)
plt.show()
plt.imshow(g)
plt.show()
plt.imshow(b)
plt.show()

```


![png](/img/teaching/computer_vision/week1/demo2/output_7_0.png)



![png](/img/teaching/computer_vision/week1/demo2/output_7_1.png)



![png](/img/teaching/computer_vision/week1/demo2/output_7_2.png)



![png](/img/teaching/computer_vision/week1/demo2/output_7_3.png)


# HSV


![](/img/teaching/computer_vision/week1/ColorSpaces/HSV.jpg)



```python
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```


```python
h = imgHSV.copy()
# set S and V channels to 255
h[:, :, 1] = 255
h[:, :, 2] = 255


s = imgHSV.copy()
# set H to 179 and V to 255 (max)
s[:, :, 0] = 179
s[:, :, 2] = 255

v = imgHSV.copy()
# set H to 179 and S to 0
v[:, :, 0] = 179
v[:, :, 1] = 0



h_RGB =  cv2.cvtColor(h,cv2.COLOR_HSV2RGB) # convert back to RGB for matplotlib to be able to plot it properly 
s_RGB =  cv2.cvtColor(s,cv2.COLOR_HSV2RGB)
v_RGB =  cv2.cvtColor(v,cv2.COLOR_HSV2RGB)

plt.imshow(RGB_im)
plt.show()
plt.imshow(h_RGB)
plt.show()
plt.imshow(s_RGB)
plt.show()
plt.imshow(v_RGB)
plt.show()

```

![png](/img/teaching/computer_vision/week1/demo2/output_10_0.png)



![png](/img/teaching/computer_vision/week1/demo2/output_10_1.png)



![png](/img/teaching/computer_vision/week1/demo2/output_10_2.png)



![png](/img/teaching/computer_vision/week1/demo2/output_10_3.png)


# LAB

![](/img/teaching/computer_vision/week1/ColorSpaces/Lab.png)


```python
imgLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
```


```python
import matplotlib.colors as clr # this library is used to create the color maps for matplotlib 


l = imgLAB.copy()
l[:, :, 1] = 0
l[:, :, 2] = 0


a = imgLAB.copy()
a[:, :, 0] = 127
a[:, :, 2] = 0

b = imgLAB.copy()
b[:, :, 0] = 127
b[:, :, 1] = 0

# here we want to result to be encoded on one channel only, so we can convert the color image into a GRAY scale image. 
# Since opencv doesnt have the LAB2GRAY converter, we have to go through the RGB format and then to GRAY
l_RGB =  cv2.cvtColor(l,cv2.COLOR_LAB2RGB)
l_GRAY = cv2.cvtColor(l_RGB,cv2.COLOR_RGB2GRAY)
a_RGB =  cv2.cvtColor(a,cv2.COLOR_LAB2RGB)
a_GRAY = cv2.cvtColor(a_RGB,cv2.COLOR_RGB2GRAY)
b_RGB =  cv2.cvtColor(b,cv2.COLOR_LAB2RGB)
b_GRAY = cv2.cvtColor(b_RGB,cv2.COLOR_RGB2GRAY)

plt.imshow(RGB_im)
plt.show()
plt.imshow(l_GRAY, cmap="gray") # L is on the gray scale
plt.show()

# the 'a' values are between red and green, so we create a colormap for matplotlib to display the color range correctly
cmap_a = clr.LinearSegmentedColormap.from_list('custom blue', ['Red',"Gray",'Green'], N=255)
plt.imshow(a_GRAY,  cmap=cmap_a)
plt.show()

# Same for 'b', between yellow and blue
cmap_b = clr.LinearSegmentedColormap.from_list('custom blue', ['Yellow',"Gray",'Blue'], N=255)
plt.imshow(b_GRAY, cmap=cmap_b)
plt.show()
```


![png](/img/teaching/computer_vision/week1/demo2/output_13_0.png)



![png](/img/teaching/computer_vision/week1/demo2/output_13_1.png)



![png](/img/teaching/computer_vision/week1/demo2/output_13_2.png)



![png](/img/teaching/computer_vision/week1/demo2/output_13_3.png)


# YCrCb


```python
imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
```


```python
# Your turn! 
# Try to display the different channels of the YCrCb format individually for our given image using the method above or another method
```
