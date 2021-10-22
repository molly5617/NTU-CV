from PIL import Image as img
import numpy as np
import cv2
import matplotlib.pyplot as plt
lena=img.open('lena.bmp')
lena_arr = np.asarray(lena)

#(a)
HW2_a=(lena_arr//128)*255
img.fromarray(HW2_a).save("HW2_a.bmp")

#(b)
m=[0]*256
for i in range(512):
    for j in range(512):
        m[lena_arr[i][j]]+=1
plt.fill(m,'black')
plt.savefig('HW2_b.jpg')

#(c)
region={}
grid=[[i//128 for i in j] for j in lena_arr]
idx=2
for i in range(512):
    for j in range(512):
        if grid[i][j]==1:
            u=i
            b=i
            l=j
            r=j
            area=1
            stack=[(i,j)]
            rows=i
            cols=j
            while stack:
                i1,j1=stack.pop()
                grid[i1][j1]=idx
                u=min(u,i1)
                b=max(b,i1)
                l=min(l,j1)
                r=max(r,j1)
                area+=1
                rows+=i1
                cols+=j1
                for x,y in [(i1,j1+1),(i1+1,j1),(i1-1,j1),(i1,j1-1)]:
                    if 0<=x<512 and 0<=y<512 and grid[x][y]==1:
                        stack.append((x,y))
            #質心座標 , 上界 , 下界 , 左界 , 右界 , 點數
            region[idx]=(rows//area,cols//area,u,b,l,r,area)
            idx+=1
result_region=[]
for i,j in region.items():
    if j[6]>500:
        result_region.append(j)

#result_region=
#[(228, 42, 0, 511, 0, 87, 35849),
# (246, 346, 0, 511, 127, 511, 205524),
# (175, 132, 94, 237, 118, 157, 3798),
# (264, 116, 237, 287, 89, 139, 1134),
# (457, 17, 399, 511, 0, 31, 2827)]

HW2_c=np.array([[[i]*3 for i in j] for j in HW2_a],dtype='uint8') #turn result in (a) to 512,512,3
for i in result_region:
    cv2.rectangle(HW2_c,(i[4],i[2]),(i[5],i[3]),(0,255,0),2)
    cv2.circle(HW2_c,(i[1],i[0]),5,(255,0,0),2)
img.fromarray(HW2_c).save("HW2_c.bmp")