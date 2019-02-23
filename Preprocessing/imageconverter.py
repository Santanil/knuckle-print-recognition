AUTHOR = "BIKRAM MODAK"

from scipy import ndimage, misc  # for i/o and converting images to numpy arrays
import numpy as np  # for working image arrays and vectors
import matplotlib.pyplot as plt  # for visualizing images
import cv2  # for various image manipulations
from skimage import restoration
from scipy.signal import convolve2d as conv2
import os
import sys
sys.path.append("..")
# import app
# import csv
# save_file_path = "dataset.csv"
# file = open(save_file_path,'w',newline= '')
# writer =csv.writer(file)

image_counter = 0

class ImageConverter:
    """Converts images to different types of data"""
    imageFIFO = []  # FIF0 to store images to be preprocessed

    def __init__(self, per_person_finger_wise_imagedir_list):

        self.m_fingerwise_imagefolder_list = []
        self.m_fingerwise_imagefolder_list = per_person_finger_wise_imagedir_list

    # fetching images of rgb format and converting them into black white format
    def convertToGrayScale(self):
        # glob function finds files with the given pattern here is the string in image_directory
        global image_counter
        try:
            for fingerimagefolder in self.m_fingerwise_imagefolder_list:
                list_of_image = os.listdir(fingerimagefolder)
                for imagenum in list_of_image[0:6]:
                    image_counter += 1
                    imagerpath = fingerimagefolder+ "\\" + imagenum
                    # print(imagerpath)
                    m_image = cv2.imread(imagerpath)
                    m_gray_image = cv2.cvtColor(m_image, cv2.COLOR_BGR2GRAY)
                    # print("Image Shape after grayscale conversion:",m_gray_image.shape,type(m_gray_image))
                    ImageConverter.imageFIFO.append(m_gray_image)
        except:
            print(str(OSError))
            print("\n--No images found!\nor\n--No Folder Found!\n")
            pass

    # adding noise into images
    def add_noise(self):
        m_temporary_image_list = []  # temporary FIFO to hold images
        m_temporary_image_list[:] = ImageConverter.imageFIFO[:]  # pushing images from main FIFO to temporary FIFO
        ImageConverter.imageFIFO[:] = []  # flushing main FIFO
        for image in m_temporary_image_list:
            # calculating and adding noise value into image pixel values
            m_noisy_image = image + 0.4 * image.std() * np.random.random(image.shape)
            ImageConverter.imageFIFO.append(m_noisy_image)
        del m_temporary_image_list  # dereferencing temporary FIFO

    # removing noise data from images
    def de_noise(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageFIFO[:]
        ImageConverter.imageFIFO[:] = []
        for image in m_temporaryImageList:
            # using medial filter to smooth image pixels
            denoised_image = ndimage.median_filter(image, size=2)
            ImageConverter.imageFIFO.append(denoised_image)
        del m_temporaryImageList

    def detectBlur(self, image):
        # compute the Laplacian of the image and then return the focus
        # measure, which is simply the variance of the Laplacian
        return cv2.Laplacian(image, cv2.CV_64F).var()

    # adding blur into images
    def addBlur(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageFIFO[:]
        ImageConverter.imageFIFO[:] = []
        for image in m_temporaryImageList:
            # using gaussian filter to smoothing images to a greater extent
            very_blurred = ndimage.gaussian_filter(image, sigma=5)
            ImageConverter.imageFIFO.append(very_blurred)
        del m_temporaryImageList

    def getBlurValue(self):
        for image in ImageConverter.imageFIFO:
            blur_value = self.detectBlur(image)
            print("--Blur Value (less is more) :", blur_value)

    # removing blurrines from images
    def deblurring(self):
        psf = np.ones((25, 25))
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageFIFO[:]
        ImageConverter.imageFIFO[:] = []
        for image in m_temporaryImageList:
            # deconvulating image data ; tbh; i don't understand this code snippet, copied from stackoverflow
            deconvolved_image = restoration.wiener(image, psf, balance=2110)
            ImageConverter.imageFIFO.append(deconvolved_image)
        del m_temporaryImageList

    # normalizing images
    # The normalization is a
    # process that changes the range of pixel intensity
    # values. Basically it has two steps
    def normalizeImages(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageFIFO[:]
        ImageConverter.imageFIFO[:] = []
        for image in m_temporaryImageList:
            normalizedImg = np.zeros(image.shape)
            normalizedImg = cv2.normalize(image, normalizedImg, 0, 255, cv2.NORM_MINMAX)
            ImageConverter.imageFIFO.append(normalizedImg)
        del m_temporaryImageList

    # to convert images into binary form (self-explanatory)
    def imageSegmentation(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageFIFO[:]
        ImageConverter.imageFIFO[:] = []
        for image in m_temporaryImageList:
            ret, thresh = cv2.threshold(image, 0, 255,
                                        cv2.THRESH_BINARY_INV +
                                        cv2.THRESH_OTSU)
            thresh[thresh == 255] = 1
            ImageConverter.imageFIFO.append(thresh)
        del m_temporaryImageList

    def compressImages(self):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        # encode to jpeg format
        # encode param image quality 0 to 100. default:95
        # if you want to shrink data size, choose low image quality.
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageFIFO[:]
        ImageConverter.imageFIFO[:] = []
        for image in m_temporaryImageList:
            result, encimg = cv2.imencode('.jpg', image, encode_param)
            if False == result:
                print('could not compress image!')
            # decode from jpeg format
            decimg = cv2.imdecode(encimg, cv2.IMREAD_UNCHANGED)
            ImageConverter.imageFIFO.append(decimg)
        del m_temporaryImageList

    # this method will convert images to a vector
    def imageToVector(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageFIFO[:]
        ImageConverter.imageFIFO[:] = []
        for image in m_temporaryImageList:
            vectorImage = image.flatten(order='K')
            ImageConverter.imageFIFO.append(vectorImage)
        del m_temporaryImageList

    @staticmethod
    def showimageFIFO():
        # global image_counter
        # print("Length of input matrix",len(ImageConverter.imageFIFO))
        # print("No of images:",image_counter)
        for imagedata in ImageConverter.imageFIFO:
            # print(imagedata.shape)
            print(imagedata)

    @staticmethod
    def showImage(imagetitle):
        for imagearray in ImageConverter.imageFIFO:
            plt.title(imagetitle)
            plt.imshow(imagearray, cmap=plt.cm.gray)
            plt.show()

    @staticmethod
    def writetodatasetfile():
        print("Writing to file.\n")
        np.savetxt("matrix.csv",ImageConverter.imageFIFO,delimiter=",",fmt="%i")

    @staticmethod
    def saveImage():
        for index, imagearray in enumerate(ImageConverter.imageFIFO):
            misc.imsave("{0}_new.jpg".format(index), imagearray)
