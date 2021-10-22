from PIL import Image as img
import numpy as np
import cv2
import matplotlib.pyplot as plt
lena=img.open('lena.bmp')
lena_arr = np.asarray(lena)

#(a)original histogram
m=[0]*256
for i in range(512):
    for j in range(512):
        m[lena_arr[i][j]]+=1
plt.bar(x=[i for i in range(256)],height=m,width=1)


#(b) 1/3
HW3_b=np.array([[i//3 for i in j] for j in lena_arr],dtype='uint8')
mb=[0]*256
for i in range(512):
    for j in range(512):
        mb[HW3_b[i][j]]+=1
plt.bar(x=[i for i in range(256)],height=mb,width=1)
cdf=[mb[0]]*256
for i in range(1,256):
    cdf[i]=mb[i]+cdf[i-1]
plt.plot(cdf)

#(c)histogram equalization
step=(512*512)//256
bound=step
newcdf=[0]*256
idx=0
d={}
while newcdf[0]<bound:
        newcdf[0]+=mb[idx]
        d[idx]=0
        idx+=1

for i in range(1,256):
    newcdf[i]=newcdf[i-1]
    bound+=step
    while newcdf[i]<bound:
        newcdf[i]+=mb[idx]
        d[idx]=i
        idx+=1
while idx<256:
    newcdf[i]+=mb[idx]
    d[idx]=i
    idx+=1

lenac=np.array([[d[i] for i in j] for j in HW3_b],dtype='uint8')
newm=[0]*256
for i in range(512):
    for j in range(512):
        newm[lenac[i][j]]+=1
plt.bar([i for i in range(256)],newm,width=1)
plt.plot(newcdf)
