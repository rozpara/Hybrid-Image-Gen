import cv2

highFreqCutoff = 35;
lowFreqCutoff = 99;

#import images as grayscale images
high = cv2.imread('paul.jpg',0)
low = cv2.imread('zach.jpg',0)

m,n = low.shape

#apply the highpass filter
blur = cv2.GaussianBlur(low, (lowFreqCutoff,lowFreqCutoff), 0)

#apply highpass gaussian filter and subtract it from the original image
blur2 = cv2.GaussianBlur(high, (highFreqCutoff, highFreqCutoff),0)
sharp = high - blur2

#show the hybrid image
cv2.imshow('img', sharp + blur)

#press anykey
cv2.waitKey(0)
