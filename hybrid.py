import cv2


high  = cv2.imread('einstein.png')
low = cv2.imread('marilyn.png')

m,n,d = low.shape

blur = cv2.GaussianBlur(low, (49,49), 0)

blur2 = cv2.GaussianBlur(high, (7,7), 0)
sharp = high - blur2

cv2.imshow('img', sharp + blur)

cv2.waitKey(0)
