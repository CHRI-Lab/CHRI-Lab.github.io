---
title: Demo Gaussian Blur 
summary: "    "
tags:
- opencv
date: "2020-01-01T00:00:00Z"

weight: 1

header:
  caption: ""
  image: ""

---



```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
```


```python
img = cv2.imread('noisyImg_1.jpg',1)
#convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
```




    <matplotlib.image.AxesImage at 0x1de43671b70>




![png](/img/teaching/computer_vision/week2/gaussian_blur/output_1_1.png)



```python
#Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),3)
plt.imshow(blur)
```




    <matplotlib.image.AxesImage at 0x1de437332e8>




![png](/img/teaching/computer_vision/week2/gaussian_blur/output_2_1.png)



```python
cv2.getGaussianKernel?
```


    [1;31mDocstring:[0m
    getGaussianKernel(ksize, sigma[, ktype]) -> retval
    .   @brief Returns Gaussian filter coefficients.
    .   
    .   The function computes and returns the \f$\texttt{ksize} \times 1\f$ matrix of Gaussian filter
    .   coefficients:
    .   
    .   \f[G_i= \alpha *e^{-(i-( \texttt{ksize} -1)/2)^2/(2* \texttt{sigma}^2)},\f]
    .   
    .   where \f$i=0..\texttt{ksize}-1\f$ and \f$\alpha\f$ is the scale factor chosen so that \f$\sum_i G_i=1\f$.
    .   
    .   Two of such generated kernels can be passed to sepFilter2D. Those functions automatically recognize
    .   smoothing kernels (a symmetrical kernel with sum of weights equal to 1) and handle them accordingly.
    .   You may also use the higher-level GaussianBlur.
    .   @param ksize Aperture size. It should be odd ( \f$\texttt{ksize} \mod 2 = 1\f$ ) and positive.
    .   @param sigma Gaussian standard deviation. If it is non-positive, it is computed from ksize as
    .   `sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8`.
    .   @param ktype Type of filter coefficients. It can be CV_32F or CV_64F .
    .   @sa  sepFilter2D, getDerivKernels, getStructuringElement, GaussianBlur
    [1;31mType:[0m      builtin_function_or_method
    



```python
#Gaussian filtering v2
G = cv2.getGaussianKernel(5,3)
print(G)

GM = G*G.T;
print(GM)
plt.matshow(GM)
plt.show()

```

    [[0.17820326]
     [0.21052227]
     [0.22254894]
     [0.21052227]
     [0.17820326]]
    [[0.0317564  0.03751576 0.03965895 0.03751576 0.0317564 ]
     [0.03751576 0.04431963 0.04685151 0.04431963 0.03751576]
     [0.03965895 0.04685151 0.04952803 0.04685151 0.03965895]
     [0.03751576 0.04431963 0.04685151 0.04431963 0.03751576]
     [0.0317564  0.03751576 0.03965895 0.03751576 0.0317564 ]]
    


![png](/img/teaching/computer_vision/week2/gaussian_blur/output_4_1.png)



```python
blur2 = cv2.filter2D(img,-1,GM)
```


```python
#show original and filtered images
plt.figure(figsize=(20,10))
plt.subplot(1,3,1),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(blur2),plt.title('Blurred 2')
plt.xticks([]), plt.yticks([])
plt.show()
```


![png](/img/teaching/computer_vision/week2/gaussian_blur/output_6_0.png)



```python

```
