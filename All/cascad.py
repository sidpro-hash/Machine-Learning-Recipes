import numpy as np
import cv2

cat_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('Cat1.jpeg')
cats = cat_cascade.detectMultiScale(gray,1.01,7)
for(x,y,w,h) in cats:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('cats',img)
cv2.waitKey(0)
cv2.destroyAllWindows()