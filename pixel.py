# https://stackoverflow.com/questions/55508615/how-to-pixelate-image-using-opencv-in-python 

import cv2
import numpy as np

# Input image
input = cv2.imread('./images/opencv_frame_0.png')

# Get input size
height, width = input.shape[:2]

# Desired "pixelated" size
w, h = (100, 100)

# Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
cv2.imshow('temp', temp)


# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

# cv2.imshow('Input', input)
cv2.imshow('Output', output)
np.savetxt('img2105.csv', output.reshape[-1,1], fmt="%s", header=str(output.shape))

cv2.waitKey(0)