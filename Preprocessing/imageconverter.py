AUTHOR = "BIKRAM MODAK"
# from PIL import Image
from glob import glob
from scipy import ndimage,misc
import numpy as np
import matplotlib.pyplot as plt

print('_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_')
print("|              IMAGE CONVERTER STARTED                |")
print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')

# other setup variables will be added later
with open("setup.config",'r') as setupfile:
    imageDir = setupfile.read()

print("\n\nLoading... ",end='')
print(imageDir)

class ImageConverter:
    # Memory to store images to be preprocessed
    imageQueue=[]
    def __init__(self,imageDir):
        self.m_imagelist = glob(imageDir+"*")

    def getOriginalImages(self):
        # glob function finds files with the given pattern here is the string in image_directory
        for imageName in self.m_imagelist:
            m_image = ndimage.imread(imageName)
            # print(m_image.shape,type(m_image))
            ImageConverter.imageQueue.append(m_image)

    def convertToGrayScale(self):
        # glob function finds files with the given pattern here is the string in image_directory
        for imageName in self.m_imagelist:
            m_image = ndimage.imread(imageName,mode = 'L')
            # print(m_image.shape,type(m_image))
            ImageConverter.imageQueue.append(m_image)

    

    @staticmethod
    def showImageQueue():
        print(ImageConverter.imageQueue)

    @staticmethod
    def showImage():
        for imagearray in ImageConverter.imageQueue:
            plt.imshow(imagearray,cmap=plt.cm.gray)
            plt.show()

    @staticmethod
    def saveImage():
        for index,imagearray in enumerate(ImageConverter.imageQueue):
            misc.imsave("{0}_new.jpg".format(index),imagearray)
        


imageConverter = ImageConverter(imageDir)
imageConverter.getOriginalImages()
imageConverter.convertToGrayScale()
ImageConverter.showImageQueue()
ImageConverter.showImage()