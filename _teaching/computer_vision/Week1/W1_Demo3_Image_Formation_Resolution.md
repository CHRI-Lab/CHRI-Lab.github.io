---
title: Demo 3 Resolution 
summary: Play with image resolution
tags:
- opencv
date: "2020-01-03T00:00:00Z"


header:
  caption: ""
  image: "/img/teaching/computer_vision/week1/demo3/minion.jpg"

---



```python
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("minion.jpg",0) # read as a grayscale image
print(img.shape)
plt.imshow(img)
plt.show()
```

    (532, 800)
    


![png](/img/teaching/computer_vision/week1/demo3/output_1_1.png)



```python
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
```


![png](/img/teaching/computer_vision/week1/demo3/output_2_0.png)



```python
cv2.imshow('Grayscale Image', img)
cv2.waitKey(0) # press any key
cv2.destroyAllWindows()

```

## Resize Image
Let's play with the resolution of this image and try to resize it.


```python
cv2.resize?
```


    [1;31mDocstring:[0m
    resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst
    .   @brief Resizes an image.
    .   
    .   The function resize resizes the image src down to or up to the specified size. Note that the
    .   initial dst type or size are not taken into account. Instead, the size and type are derived from
    .   the `src`,`dsize`,`fx`, and `fy`. If you want to resize src so that it fits the pre-created dst,
    .   you may call the function as follows:
    .   @code
    .   // explicitly specify dsize=dst.size(); fx and fy will be computed from that.
    .   resize(src, dst, dst.size(), 0, 0, interpolation);
    .   @endcode
    .   If you want to decimate the image by factor of 2 in each direction, you can call the function this
    .   way:
    .   @code
    .   // specify fx and fy and let the function compute the destination image size.
    .   resize(src, dst, Size(), 0.5, 0.5, interpolation);
    .   @endcode
    .   To shrink an image, it will generally look best with #INTER_AREA interpolation, whereas to
    .   enlarge an image, it will generally look best with c#INTER_CUBIC (slow) or #INTER_LINEAR
    .   (faster but still looks OK).
    .   
    .   @param src input image.
    .   @param dst output image; it has the size dsize (when it is non-zero) or the size computed from
    .   src.size(), fx, and fy; the type of dst is the same as of src.
    .   @param dsize output image size; if it equals zero, it is computed as:
    .   \f[\texttt{dsize = Size(round(fx*src.cols), round(fy*src.rows))}\f]
    .   Either dsize or both fx and fy must be non-zero.
    .   @param fx scale factor along the horizontal axis; when it equals 0, it is computed as
    .   \f[\texttt{(double)dsize.width/src.cols}\f]
    .   @param fy scale factor along the vertical axis; when it equals 0, it is computed as
    .   \f[\texttt{(double)dsize.height/src.rows}\f]
    .   @param interpolation interpolation method, see #InterpolationFlags
    .   
    .   @sa  warpAffine, warpPerspective, remap
    [1;31mType:[0m      builtin_function_or_method
    



```python
half = cv2.resize(img, None, fx=0.5, fy=0.5)
print(half.shape)
plt.imshow(half,  cmap='gray', vmin=0, vmax=255)
plt.show()
```

    (266, 400)
    


![png](/img/teaching/computer_vision/week1/demo3/output_6_1.png)



```python
# if you run this cell several times, you will see the resolution decreasing very fast.
half = cv2.resize(half, None, fx=0.5, fy=0.5)
print(half.shape)
plt.imshow(half,  cmap='gray', vmin=0, vmax=255)
plt.show()

```

    (133, 200)
    


![png](/img/teaching/computer_vision/week1/demo3/output_7_1.png)



```python
half.shape
```




    (133, 200)




```python
half.size
```




    26600




```python
half.dtype
```
