import cv2
import numpy as np
from PIL import Image
import argparse
from sklearn.cluster import DBSCAN

def apply_filter_to_pixel(filter, frame):
    #apply filter to the frame
    
    return filter

#lower masking should be lowest hue possible, moderately high saturation, and medium brightness
lower=np.array([0,150,150])
upper=np.array([180,255,255])

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
    
h, w, c = frame.shape

# holds all black pixels, until a pixel is updated with its filter color
filter = np.zeros((h,w,c), dtype=np.uint8)

while True:

    ret, frame = cap.read()
    
    frame = cv2.resize(frame, (480,360))

    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #make a masked image
    fullMask = cv2.inRange(hsvImage, lower, upper)

    # image that will be shown
    ret = np.zeros((h,w,c), dtype=np.uint8)

    # iterates through every pixel
    for y in range(h):
        for x in range(w):
            # if the pixel is part of the mask, add it to the filter
            if fullMask[y,x] == 255:
                filter[y,x] = frame[y,x]
            # isolate the current pixel tint
            cur = filter[y,x]    
            # tint is not black, so set the filter
            if cur[0] != 0 and cur[1] != 0 and cur[2] != 0:
                # tint the current pixel
                ret[y,x] = cur*0.8 + frame[y,x]*0.2
            else:
                ret[y,x] = frame[y,x]

                
    cv2.imshow('fullMask', fullMask)
    cv2.imshow('frame', frame)
    cv2.imshow('ret', ret)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
