import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpeg')

cv.imshow('Cat', img)





cv.waitKey(0)