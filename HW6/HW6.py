from PIL import Image as img
import numpy as np
import cv2
import matplotlib.pyplot as plt
lena=img.open('lena.bmp')
lena_arr = np.asarray(lena)


def expan_zero(arr):
    m=len(arr)
    n=len(arr[0])
    res=res=[[0]*(n+2) for i in range(m+2)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            res[i][j]=arr[i-1][j-1]
    return res
def h(b,c,d,e):
    if b!=c:
        return 's'
    else:
        if d==b and e==b:
            return 'r'
        else:
            return 'q'
def f(a1,a2,a3,a4):
    if a1=='r' and a2=='r'and a3=='r'and a4=='r':
        return 5
    tmp=0
    if a1=='q':
        tmp+=1
    if a2=='q':
        tmp+=1
    if a3=='q':
        tmp+=1
    if a4=='q':
        tmp+=1
    return tmp

def yokoi(lena):
    m=len(lena)
    n=len(lena[0])
    arr=[[0]*(m//8) for i in range(n//8)]
    for i in range(m//8):
        for j in range(n//8):
            arr[i][j] = lena[8*i][8*j]
    m=len(arr)
    n=len(arr[0])
    arr=expan_zero(arr)
    
    for i in range(m):
        for j in range(n):
            a1=h(arr[i+1][j+1],arr[i+1][j+2],arr[i][j+2],arr[i][j+1])
            a2=h(arr[i+1][j+1],arr[i][j+1],arr[i][j],arr[i+1][j])
            a3=h(arr[i+1][j+1],arr[i+1][j],arr[i+2][j],arr[i+2][j+1])
            a4=h(arr[i+1][j+1],arr[i+2][j+1],arr[i+2][j+2],arr[i+1][j+2])
            tmp=f(a1,a2,a3,a4)
            if tmp and arr[i][j]:
                print(f(a1,a2,a3,a4),end='')
            else:
                print(' ',end='')
        print('')
yokoi(lena_arr//128)