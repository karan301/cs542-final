from os import listdir
from os.path import isfile, join
import numpy as np
import cv2
from PIL import Image

#I'm slicing a picture into as many 30x30 patches as I can
img = Image.open("/Users/sibozhu/DeepLearning/testing/test2.jpg")
(imageWidth, imageHeight)=img.size
gridx=30
gridy=30
rangex=img.width/gridx
rangey=img.height/gridy

for x in xrange(rangex):
    for y in xrange(rangey):
        bbox=(x*gridx, y*gridy, x*gridx+gridx, y*gridy+gridy)
        slice_bit=img.crop(bbox)
        slice_bit.save('/Users/sibozhu/DeepLearning/testing/tests/'+str(x)+','+str(y)+'.jpg', optimize=True, bits=6)

print("finished slicing")


#Applying motionblur to all pictures in this folder
#Would implement pseudo random motionblur in near future
mypath='/Users/sibozhu/DeepLearning/testing/motion/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
# print(listdir(mypath))

images = np.empty(len(onlyfiles), dtype=object)

#Since the .DS_Store file is in the first place of the list,
# I have to skip that by putting start of for loop at location 1
for n in range(1, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
  size = 15

  # generating the kernel
  kernel_motion_blur = np.zeros((size, size))
  kernel_motion_blur[int((size - 1) / 2), :] = np.ones(size)
  kernel_motion_blur = kernel_motion_blur / size


  # applying the kernel to the input image
  output = cv2.filter2D(images[n], -1, kernel_motion_blur)

  cv2.imwrite('/Users/sibozhu/DeepLearning/testing/motion/'+str(onlyfiles[n]), output)

print('finished motion blurry')

