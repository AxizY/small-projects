import cv2 # a module/library for handling images
import math # a module/library for handling math functions etc
import os # a built-in library for handling everything (terminal commands)
import sys # for handling terminal arguments
values="" # an empty string/text
f=open("pixeldata.txt", "a+")
img = cv2.imread(str(sys.argv[1]).encode('unicode-escape').decode(), 0) # specifies image location on computer - converts image to grayscale
for y in range(0, img.shape[0]): # for every y
  for x in range(0, img.shape[1]): # for every x in that y
    values+=str(math.floor(img[y,x]/int(sys.argv[2]))) # adds (the pixel grayscale value divided by the y is then rounded up) to the string
  values+="\n" # adds a new line to the string
open("pixeldata.txt", 'w').close() # clears file content
f.write(values) # writes the new values
print("Values have been appended/replaced!") # prints out the results/ the string
os.system("open pixeldata.txt") # opens textedit, may not work on windows
# to run do
# python3 scriptlocation imagelocation 120
# in terminal ex.
# python3 image-compress.py avenger.png 120
