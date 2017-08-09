import sys
from os import listdir
from os.path import isfile, join
import numpy as np
import cv2
from PIL import Image
import operator



mypath = "/Users/sibozhu/DeepLearning/testing/tests/"
respath = "/Users/sibozhu/DeepLearning/testing/tests_res/"
# print(listdir(mypath))
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = map(Image.open, [mypath+'0,0.jpg', mypath+'1,0.jpg', mypath+'2,0.jpg',mypath+'0,1.jpg', mypath+'1,1.jpg', mypath+'2,1.jpg'])
print(images[0])
widths, heights = zip(*(i.size for i in images))

#trying to get the height of the total picture before merge back
heightcounter = {}
for i in range(1,len(onlyfiles)):
  for j in range(len(onlyfiles[i])):
    if onlyfiles[i][j]==",":
      heightcounter[i] = int(onlyfiles[i][0:j])

height = heightcounter[max(heightcounter, key=heightcounter.get)]

#trying to get the width of the total picture before merge b ack
widthscounter = {}
for i in range(1,len(onlyfiles)):
  for j in range(len(onlyfiles[i])):
    if onlyfiles[i][j]==",":
      widthscounter[i] = int(onlyfiles[i][j+1:-4])

width = widthscounter[max(widthscounter, key=widthscounter.get)]



# total_width = width*30
# total_height = height*30
total_width = 3*30
total_height = 2*30

new_im = Image.new('RGB', (total_width, total_height))

x_offset = 0
y_offset = 0

# for i in range(2):
#   for j in range(3):
#     im = images
#     new_im.paste(im, (x_offset,y_offset))
#     x_offset += im.size[0]


new_im.save(respath+'test.jpg')