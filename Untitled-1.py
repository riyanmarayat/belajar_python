import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('/home/marayat/Documents/pythonworkspace/image.png')
im = np.double(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))/255
c=0.7



for i in range(im.shape[0]): 
    for j in range(im.shape[1]):   
        im[i,j]=im[i,j]+c
        
 
im = im+c

       
        
        
cv2.imshow('frame', img)
        
ch= cv2.waitKey(0) & 0xFF