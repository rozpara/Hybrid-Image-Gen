import cv2

#import images
high = cv2.imread('paul.jpg',0)
low = cv2.imread('zach.jpg',0)

m,n = low.shape

#apply the highpass filter
blur = cv2.GaussianBlur(low, (111,111), 0)

#apply highpass gaussian filter and subtract it from the original image
blur2 = cv2.GaussianBlur(high, (35,35),0)
sharp = high - blur2

#show the hybrid image
cv2.imshow('img', sharp + blur)

#press anykey
cv2.waitKey(0)
