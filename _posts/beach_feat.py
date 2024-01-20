
import numpy as np
import cv2 as cv


frame = cv.imread("coogee.png")
frame = frame[200:,700:]
cv.imshow('frame',frame)

# It converts the BGR color space of image to HSV color space 
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 

lower_white = np.array([220, 220, 50]) 
upper_white = np.array([255, 255, 255]) 

lower_blue = np.array([80, 0, 0]) 
upper_blue = np.array([130, 240, 240]) 


# preparing the mask to overlay 
mask = cv.inRange(hsv, lower_blue, upper_blue) 
    
# The black region in the mask has the value of 0, 
# so when multiplied with original image removes all non-blue regions 
result = cv.bitwise_and(frame, frame, mask = mask) 

hsv = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
mm = cv.inRange(hsv, lower_white, upper_white) 
result_w = cv.bitwise_and(frame, frame, mask = mm) 


result = cv.bitwise_and(frame, frame, mask = mask) 


# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 3,
                       blockSize = 3 )


old_gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
cv.imshow('hsv',old_gray)
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
p0 = np.float32(p0)
print(p0)
while(1):
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break