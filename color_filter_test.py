import cv2
import numpy as np
from PIL import Image
import argparse
from sklearn.cluster import DBSCAN

def apply_filter_to_pixel(filter, frame, x, y, color):
    # Apply filter to the pixel at location (x, y)
    filter[y, x] = color

# Lower masking should be lowest hue possible, moderately high saturation, and medium brightness
lower = np.array([0, 180, 50])
upper = np.array([180, 255, 255])

# Video feed
cap = cv2.VideoCapture(0)
ekernel = np.ones((3, 3), np.uint8)
dkernel = np.ones((5, 5), np.uint8)

ret, frame = cap.read()

# Get the dimensions of the frame
h, w, c = frame.shape

# Holds all black pixels, until a pixel is updated with its filter color
filter = np.zeros((h, w, c), dtype=np.uint8)

# Holds the most recent sufficiently saturated pixel at each location (x, y)
recent_pixels = np.zeros((h, w, c), dtype=np.uint8)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Make a masked image
    fullMask = cv2.inRange(hsvImage, lower, upper)

    # Iterate through every pixel
    for y in range(h):
        for x in range(w):
            # If the pixel is part of the mask, update the recent_pixels array
            if fullMask[y, x] == 1:
                recent_pixels[y, x] = frame[y, x]

            # Apply the recent_pixel as a tint to the current pixel
            cur = filter[y, x]
            if cur[0] != 0 and cur[1] != 0 and cur[2] != 0:
                filter[y, x] = cur * 0.8 + recent_pixels[y, x] * 0.2

    cv2.imshow('fullMask', fullMask)
    cv2.imshow('frame', frame)
    cv2.imshow('filter', filter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()