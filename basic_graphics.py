# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:48:28 2016

@author: farmer
"""

import cv2
import numpy as np

ix,iy=-1,-1
point=np.array([])
i=0
def draw_poly(event,x,y,flags,param):
    global ix,iy,drawing,mode,point,i,img
     
    if event==cv2.EVENT_RBUTTONDBLCLK:
        ix,iy = x,y
        point = np.append(point,np.array([x,y]))
        i+=1
        point.resize((i,2))
        point = np.int32(point)
        cv2.polylines(img,[point],True,(255,0,0),1)
        cv2.imshow('image',img)
         
     # 当按下左键是返回起始位置坐标
    elif event==cv2.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        point = np.append(point,np.array([x,y]))
        i+=1
        point.resize((i,2))
        point = np.int32(point)
        cv2.polylines(img,[point],False,(255,0,0),1)
        cv2.imshow('image',img)

#img=np.zeros((512,512,3))
img=cv2.imread("g:\\face\\11.jpg")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_poly)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
#point.resize((i,2))
#point = np.int32(point)
#img2=np.zeros((512,512,3))
#cv2.namedWindow('img2')
#pts=np.array([[50,100],[150,150],[170,120],[250,210],[250,310]])
#cv2.polylines(img,[point],True,(255,0,255),2)
result=np.ones((len(point),3))
r=0
for p in point:
    result[r]=img[[0],p[1]]
    r+=1
print result
#cv2.imshow('img',img)
#cv2.waitKey(0)
#print point

cv2.destroyAllWindows()