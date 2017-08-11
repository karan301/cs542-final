from PIL import Image
img = Image.open("/Users/sibozhu/DeepLearning/testing/tests/test2.jpg")
(imageWidth, imageHeight)=img.size
gridx=30
gridy=30
rangex=img.width/gridx
rangey=img.height/gridy
print rangex*rangey
for x in xrange(rangex):
    for y in xrange(rangey):
        bbox=(x*gridx, y*gridy, x*gridx+gridx, y*gridy+gridy)
        slice_bit=img.crop(bbox)
        slice_bit.save('/Users/sibozhu/DeepLearning/testing/motion/'+str(x)+'_'+str(y)+'.jpg', optimize=True, bits=6)
