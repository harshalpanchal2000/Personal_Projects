#!/usr/bin/env python
# coding: utf-8

# In[8]:


# get_ipython().system('pip install opencv-python')
# get_ipython().system('pip install imutils')
# get_ipython().system('pip install scikit-image')


# In[1]:


import cv2
import numpy as np 
import imutils


# In[2]:


img1 = cv2.imread("C:\\Users\\pc\\Downloads\\WhatsApp Image 2022-02-26 at 11.00.16.jpeg")
img1= cv2.resize (img1, (690,300))
img2 = cv2.imread("C:\\Users\\pc\\Downloads\\WhatsApp Image 2022-02-26 at 11.00.30.jpeg")
img2= cv2.resize (img2, (690,300))

cv2.imshow("org", img1)

cv2.imshow("edit", img2)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

diff= cv2.absdiff(gray1, gray2)
cv2.imshow('diff(img1, img2)', diff)


# In[5]:


thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow('Threshold', thresh)


# In[ ]:


#Dilations
kernel = np.ones ((5,5), np.uint8)
dilate = cv2.dilate(thresh, kernel, iterations=2)
cv2.imshow("Dilation",dilate)


# In[ ]:


#Find contours
contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)


# In[ ]:


# Loop over each contour
for contour in contours:
        if cv2.contourArea(contour) > 100 :
            # calculating bounding box
            x, y, w, h= cv2.boundingRect(contour)
            #drawing boxes
            cv2.rectangle(img1, (x,y), (x+w, y+h), (0,0,255),2)
            cv2.rectangle(img2, (x,y), (x+w, y+h), (0,0,255),2)


# In[ ]:


x= np.zeros((360,10,3), np.uint8)
# result=np.hstack(img1, x, img2)
result=np.hstack(x)
cv2.imshow("Differences", result)

