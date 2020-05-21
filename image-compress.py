import cv2
import math
def compress(num,n):return(math.ceil(num/n))
values = []
img = cv2.imread(r'photo', 0)
x=0;y=0;a=0;k=0
for y in range(0, img.shape[0]):
  for x in range(0, img.shape[1]):
    values.append(compress(img[y,x],img.shape[0])) 
for a in range(0,compress(len(values),img.shape[1])):
  k = a-1
  print(values[img.shape[1]*k:a*img.shape[1]])
