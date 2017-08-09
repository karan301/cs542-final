# from __future__ import print_function
# import os
# import sys
# from os import listdir
# from os.path import isfile, join
# import numpy as np
# import cv2
# import operator
#
# from os import walk
# import glob
# from PIL import Image
#
# mypath = "/Users/sibozhu/DeepLearning/testing/tests/"
#
#
# #listing files method #0
#
# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
#     break
#
# #listing files method #1
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#
# #listing files method #2
# files = ["/Users/sibozhu/DeepLearning/testing/JR.jpg","/Users/sibozhu/DeepLearning/testing/test2.jpg","/Users/sibozhu/DeepLearning/testing/JR_blur.jpg"]
#
# #listing files method #3
#
# flag=glob.glob("/Users/sibozhu/DeepLearning/testing/tests/*.jpg")
#
# #trying to get the height of the total picture before merge back
# heightcounter = {}
# for i in range(1,len(onlyfiles)):
#   for j in range(len(onlyfiles[i])):
#     if onlyfiles[i][j]==",":
#       heightcounter[i] = int(onlyfiles[i][0:j])
#
# height = heightcounter[max(heightcounter, key=heightcounter.get)]
#
# #trying to get the width of the total picture before merge b ack
# widthscounter = {}
# for i in range(1,len(onlyfiles)):
#   for j in range(len(onlyfiles[i])):
#     if onlyfiles[i][j]==",":
#       widthscounter[i] = int(onlyfiles[i][j+1:-4])
#
# width = widthscounter[max(widthscounter, key=widthscounter.get)]
#
#
#
# # total_width = width*30
# # total_height = height*30
# total_width = width*30
# total_height = height*30
#
# result = Image.new("RGB", (800, 800))
#
# for index, file in enumerate(flag):
#
#   path = os.path.expanduser(file)
#   img = Image.open(path)
#   print(file)
#   img.thumbnail((400, 400), Image.ANTIALIAS)
#   x = index // 2 * 400
#   y = index % 2 * 400
#   w, h = img.size
#   # print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
#   result.paste(img, (x, y, x + w, y + h))
#
# result.save(os.path.expanduser('/Users/sibozhu/DeepLearning/testing/tests_res/res.jpg'))
import sys
print(sys.path)
import cv2
import numpy as np
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7")
from matplotlib import pyplot as plt
from scipy.misc import imsave
# import scipy
from scipy import ndimage
from scipy import misc
import scipy.misc
import scipy

import argparse
import image_slicer
from image_slicer import join


img = '/Users/sibozhu/DeepLearning/testing/JR.jpg'
num_tiles = 64
tiles = image_slicer.slice(img, num_tiles)



file = "JR"
k = 0
filelist =[]
for i in range(1,9):
    for j in range(1,9):
        filelist.insert(k, file+"_"+str(i).zfill(2)+"_"+str(j).zfill(2)+".jpg")
        k=k+1

for i in range(0,num_tiles):
    img = scipy.misc.imread(filelist[i])
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf *hist.max()/ cdf.max()
    plt.plot(cdf_normalized, color = 'g')
    plt.hist(img.flatten(),256,[0,256], color = 'g')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_o = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_o,0).astype('uint8')
    img3 = cdf[img]
    cv2.imwrite(filelist[i],img3)


image = join(tiles)
image.save('/Users/sibozhu/DeepLearning/testing/tests_res/JR_res.jpg')