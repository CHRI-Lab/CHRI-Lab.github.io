---
title:  Demo Fourier Transform and Frequency filtering 
summary: "  "
tags:
- opencv
date: "2020-01-01T00:00:00Z"


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
img = cv2.imread('minion.jpg',1)
#convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show the image
plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.imshow(img, cmap = "gray")

# display the historgram
plt.subplot(1,2,2)
plt.hist(img.flatten())
plt.show()
```


![png](/img/teaching/computer_vision/week2/fourier/output_2_0.png)



```python
# create the centering matrix
centering_m = np.full((img.shape[0] , img.shape[1]), -1)

for x in range(0,img.shape[0]):
    for y in range(0,img.shape[1]):
        centering_m[x,y] = (-1)**(x+y)
        
plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.imshow(centering_m[0:10,0:10])
plt.subplot(1,2,2)
plt.hist(centering_m.flat)
plt.show()

```


![png](/img/teaching/computer_vision/week2/fourier/output_3_0.png)



```python
centered_img = img *centering_m
plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.imshow(centered_img, cmap = "gray")
plt.subplot(1,2,2)
plt.hist(centered_img.flatten())
plt.show()
```


![png](/img/teaching/computer_vision/week2/fourier/output_4_0.png)



```python
# compute the 2D FFT
dft =  np.fft.fft2(centered_img)
plt.figure(figsize=(20,10))
plt.imshow(np.log(1+np.abs(dft)), cmap = "gray")

```




    <matplotlib.image.AxesImage at 0x1dfe72c33c8>




![png](/img/teaching/computer_vision/week2/fourier/output_5_1.png)



```python
def distance(point1,point2):
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
```

## Filters

## Ideal LowPass Filter
![](/img/teaching/computer_vision/week2/fourier/equations/idealLP.png)


```python
def idealFilterLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 1
    return base

plt.imshow(idealFilterLP(50,img.shape), cmap='gray'),plt.title('Low Pass Filter')
plt.show()
```


![png](/img/teaching/computer_vision/week2/fourier/output_9_0.png)


## Ideal HighPass Filter
![](/img/teaching/computer_vision/week2/fourier/equations/idealHP.png)


```python
def idealFilterHP(D0,imgShape):
    base = np.ones(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 0
    return base


plt.imshow(idealFilterHP(50,img.shape), cmap='gray'),plt.title('High Pass Filter')
plt.show()
```


![png](/img/teaching/computer_vision/week2/fourier/output_11_0.png)


## Gaussian LowPass Filter
![](/img/teaching/computer_vision/week2/fourier/equations/gaussianLP.png)


```python
def gaussianLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = np.exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

plt.imshow(gaussianLP(80,img.shape), cmap='gray'),plt.title('Gaussian Low Pass Filter')
plt.xticks([]), plt.yticks([])
plt.show()
```


![png](/img/teaching/computer_vision/week2/fourier/output_13_0.png)


## Gaussian HighPass Filter
![](/img/teaching/computer_vision/week2/fourier/equations/gaussianHP.png)


```python
def gaussianHP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1 - np.exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

plt.imshow(gaussianHP(80,img.shape), cmap='gray'),plt.title('Gaussian High Pass Filter')
plt.xticks([]), plt.yticks([])
plt.show()
```


![png](/img/teaching/computer_vision/week2/fourier/output_15_0.png)


## Apply Filter on DFT


```python
# filter the DFT
fdft = dft * idealFilterLP(50,img.shape) ## note that we do a multiplication cause we are in the frequency domain

# inverse the filtered DFT
idft = np.fft.ifft2(fdft)

# take the real part and de center it
real_centered = idft.real * centering_m

plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.imshow(np.log(1+np.abs(fdft)), cmap = "gray")
plt.title('Filtered DFT')
plt.subplot(1,2,2)
plt.imshow(real_centered, cmap = "gray",vmin=0, vmax=255)
plt.title('Inversed Filtered DFT')
plt.show()

```


![png](/img/teaching/computer_vision/week2/fourier/output_17_0.png)



```python
# filter the DFT
fdft = dft * gaussianLP(50,img.shape)

# inverse the filtered DFT
idft = np.fft.ifft2(fdft)

# take the real part and de center it
real_centered = idft.real * centering_m

plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.imshow(np.log(1+np.abs(fdft)), cmap = "gray")
plt.title('Filtered DFT')
plt.subplot(1,2,2)
plt.imshow(real_centered, cmap = "gray", vmin=0, vmax=255)
plt.title('Inversed Filtered DFT')
plt.show()
```


![png](/img/teaching/computer_vision/week2/fourier/output_18_0.png)


## Demonstraring that we can go back and forth from image to frequency without loss


```python
# inverse the filtered DFT
idft = np.fft.ifft2(dft)

# take the real part and de center it
real_centered = idft.real * centering_m


plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.imshow(img, cmap = "gray")
plt.title(' Original Image')
plt.subplot(1,2,2)
plt.imshow(real_centered, cmap = "gray", vmin=0, vmax=255)
plt.title('Inversed DFT')
plt.show()

plt.imshow(real_centered - img, cmap = "gray", vmin=0, vmax=255)
plt.title('Difference')
plt.show()
```


![png](/img/teaching/computer_vision/week2/fourier/output_20_0.png)



![png](/img/teaching/computer_vision/week2/fourier/output_20_1.png)



