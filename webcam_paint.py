import cv2
import numpy as np
from PIL import Image
import argparse
from sklearn.cluster import DBSCAN

def apply_filter_to_pixel(filter, frame):
    #apply filter to the frame
    
    return filter

#lower masking should be lowest hue possible, moderately high saturation, and medium brightness
lower=np.array([0,150, 100])
upper=np.array([179,255,255])

#video feed
cap = cv2.VideoCapture(0)
ekernel = np.ones((3,3), np.uint8)
dkernel = np.ones((9,9), np.uint8)


ret, frame = cap.read()

    #get the dimensions of the frame

h, w, c = frame.shape
 
# holds all black pixels, until a pixel is updated with its filter color
filter = np.zeros((h,w,c), dtype=np.uint8)

while True:
    ret, frame = cap.read()
    #convert to hsv
    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #make a masked image
    fullMask = cv2.inRange(hsvImage, lower, upper)
    # After creating the mask
    cv2.imshow('Mask', fullMask)    
    
    # eroded = cv2.erode(fullMask, kernel=ekernel, iterations=1)
    dilated = cv2.dilate(fullMask, kernel=dkernel, iterations=1)
    
    cv2.imshow('dilated', dilated) 

    # image that will be shown
    retImg = np.zeros((h,w,c), dtype=np.uint8)
    
    mask = dilated == 255


    # Update the filter where the mask is True
    filter[mask] = filter[mask] * 0.5 + frame[mask] * 0.5

    # Create a boolean mask for non-black pixels in the filter
    non_black_mask = np.any(filter != 0, axis=2)
    
    # Create the retImg
    retImg = np.where(non_black_mask[:,:,np.newaxis], 
                      (filter * 0.5 + frame * 0.5).astype(np.uint8), 
                      frame)
    
    cv2.imshow('retImg', retImg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()