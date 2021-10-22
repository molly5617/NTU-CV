from PIL import Image as img
import numpy as np
import cv2

lena=img.open('/Users/wangyiyao/NTU-CV/lena.bmp')
lena_arr = np.asarray(lena)

HW1_a=lena_arr[::-1]

HW1_b=np.array([i[::-1] for i in lena_arr])

HW1_c=lena_arr.T

rotate = cv2.getRotationMatrix2D((256,256), 45, 1)
HW1_d=cv2.warpAffine(lena_arr,rotate,(512,512))

tmp=np.array(lena_arr,dtype='int')#avoid overflow in unsign 8 bit
HW1_e=[[(tmp[i*2][j*2]+tmp[i*2+1][j*2]+tmp[i*2][j*2+1]+tmp[i*2+1][j*2+1])//4 for j in range(256)] for i in range(256)]
HW1_e=np.array(HW1_e,dtype='uint8')

HW1_f=(lena_arr//128)*255

img.fromarray(HW1_a).save("HW1_a.bmp")
img.fromarray(HW1_b).save("HW1_b.bmp")
img.fromarray(HW1_c).save("HW1_c.bmp")
img.fromarray(HW1_d).save("HW1_d.bmp")
img.fromarray(HW1_e).save("HW1_e.bmp")
img.fromarray(HW1_f).save("HW1_f.bmp")