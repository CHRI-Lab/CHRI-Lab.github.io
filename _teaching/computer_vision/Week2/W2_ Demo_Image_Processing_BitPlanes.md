---
title: Demo Bit-Planes 
summary: "  "
tags:
- opencv
date: "2020-01-01T00:00:00Z"


header:
  caption: ""
  image: "teaching/computer_vision/week2/bitplanes/bitplane_slide.png"

type: book

---




```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
```


```python
img = cv2.imread('minion.jpg',0)
plt.figure(figsize=(20,10))

plt.imshow(img,'gray')

plt.show()
```


![svg](/img/teaching/computer_vision/week2/bitplanes/output_2_0.svg)



```python
out = []
plt.figure(figsize=(30,20))
for k in range(0, 8):
    # create an image for each k bit plane
    plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
    # execute bitwise and operation
    res = cv2.bitwise_and(plane, img)
    # multiply ones (bit plane sliced) with 255 just for better visualization
    x = cv2.equalizeHist(res)
    out.append(res)
    plt.subplot(1,8,k+1),plt.imshow(res,'gray'),plt.title("plane "+str(k))
    plt.xticks([]), plt.yticks([])

plt.show()
```


![svg](/img/teaching/computer_vision/week2/bitplanes/output_3_0.svg)



```python
ms_planes = out[-1] +out[-2] +out[-3]
plt.imshow(ms_planes,'gray'),plt.title(" plane 5-7")
```




    (<matplotlib.image.AxesImage at 0x243a2f83be0>, Text(0.5, 1.0, ' plane 5-7'))




![svg](/img/teaching/computer_vision/week2/bitplanes/output_4_1.svg)



```python

```
