import cv2 as cv
import numpy as np

# https://www.javatpoint.com/opencv

blank = np.zeros((500,500,3),dtype='uint8')
# uint8 is image type
cv.imshow('Blank',blank)

blank[200:300,300:400]=0,255,0
cv.imshow('Green',blank) 


cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)

cv.circle(blank,(250,250),50,(255,255,0),thickness=-3)
cv.imshow('Rectangle',blank)

cv.line(blank,(0,0),(250,250),(255,255,255),thickness=7)
cv.imshow('line',blank)
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),2)

cv.waitKey(0)





img=cv.imread('Electricity.png')
gray=cv.cvtColor(img,cv.COLOR_BAYER_BG2BGR)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blurred',blur)


