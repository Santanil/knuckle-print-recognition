AUTHOR = "BIKRAM MODAK"

from glob import glob
from scipy import ndimage,misc
import numpy as np
import matplotlib.pyplot as plt
# For blur detection
import cv2

# For deblurring
from skimage import restoration
from scipy.signal import convolve2d as conv2

class ImageConverter:
    # Memory to store images to be preprocessed
    imageQueue=[]
    def __init__(self,imageDir):
        print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_')
        print('|              IMAGE CONVERTER EXECUTING              ')
        print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_')
        self.m_imagelist = glob(imageDir+"*")

    def getOriginalImages(self):
        # glob function finds files with the given pattern here is the string in image_directory
        for imageName in self.m_imagelist:
            m_image = ndimage.imread(imageName)
            # print("Image Shape:",m_image.shape,type(m_image))
            ImageConverter.imageQueue.append(m_image)

    def convertToGrayScale(self):
        # glob function finds files with the given pattern here is the string in image_directory
        for imageName in self.m_imagelist:
            m_image = cv2.imread(imageName)
            m_gray_image = cv2.cvtColor(m_image, cv2.COLOR_BGR2GRAY)
            # print("Image Shape after grayscale conversion:",m_gray_image.shape,type(m_gray_image))
            ImageConverter.imageQueue.append(m_gray_image)

    def add_noise(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageQueue[:]
        ImageConverter.imageQueue[:] = []
        for imagearray in m_temporaryImageList:
            m_noisy_image = imagearray + 0.4 * imagearray.std() * np.random.random(imagearray.shape)
            ImageConverter.imageQueue.append(m_noisy_image)
        del m_temporaryImageList

    def de_noise(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageQueue[:]
        ImageConverter.imageQueue[:] = []
        for noisy in m_temporaryImageList:
            denoised_image = ndimage.median_filter(noisy,2)
            ImageConverter.imageQueue.append(denoised_image)
        del m_temporaryImageList

    def detectBlur(self,image):
        # compute the Laplacian of the image and then return the focus
        # measure, which is simply the variance of the Laplacian
        return cv2.Laplacian(image, cv2.CV_64F).var()

    def addBlur(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageQueue[:]
        ImageConverter.imageQueue[:] = []
        for image in m_temporaryImageList:
            very_blurred = ndimage.gaussian_filter(image,sigma=5)
            ImageConverter.imageQueue.append(very_blurred)
        del m_temporaryImageList

    def getBlurValue(self):
        for imagearray in ImageConverter.imageQueue:
            blur_value = self.detectBlur(imagearray)
            print("--Blur Value (less is more) :", blur_value)

    def deblurring(self):
        psf = np.ones((25, 25))
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageQueue[:]
        ImageConverter.imageQueue[:] = []
        for image in m_temporaryImageList:
            deconvolved_image = restoration.wiener(image, psf , balance = 2110)
            ImageConverter.imageQueue.append(deconvolved_image)
        del m_temporaryImageList

    def normalizeImages(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageQueue[:]
        ImageConverter.imageQueue[:] = []
        for image in m_temporaryImageList:
            normalizedImg = np.zeros(image.shape)
            normalizedImg = cv2.normalize(image,  normalizedImg, 0, 255, cv2.NORM_MINMAX)
            ImageConverter.imageQueue.append(normalizedImg)
        del m_temporaryImageList
        
    @staticmethod
    def showImageQueue():
        for i in ImageConverter.imageQueue:
            print(i)

    @staticmethod
    def showImage(imagetitle):
        for imagearray in ImageConverter.imageQueue:
            plt.title(imagetitle)
            plt.imshow(imagearray,cmap=plt.cm.gray)
            plt.show()

    @staticmethod
    def saveImage():
        for index,imagearray in enumerate(ImageConverter.imageQueue):
            misc.imsave("saved_images\\{0}_new.jpg".format(index),imagearray)