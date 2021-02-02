import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('photos/cat.jpeg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

print(img.shape) #3 color channel
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

# plt.imshow(img)
# plt.show()



cv.waitKey(0)
