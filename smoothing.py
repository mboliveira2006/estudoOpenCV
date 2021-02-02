import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)

# Averaging 
#average = cv.blur(img, (7,7))
average = cv.blur(img, (3,3))
cv.imshow('Average blur', average)

# Gaussian Blur
# gauss = cv.GaussianBlur(img, (7,7), 0)
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

# Median blur
# median = cv.medianBlur(img, 7)
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 1, 35, 25)
cv.imshow('Bilateral', bilateral)

# plt.imshow(img)
# plt.show()


cv.waitKey(0)
