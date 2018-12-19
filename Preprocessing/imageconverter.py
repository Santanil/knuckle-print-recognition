AUTHOR = "BIKRAM MODAK"
from PIL import Image
from glob import glob

imageDir="C:\\Users\\bmodak\\Videos\\KPR-Confidential-Top-Secret\\knuckle-print-recognition\\images\\"

print('_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_')
print("|              IMAGE CONVERTER STARTED                |")
print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')

class ImageConverter:
    # Memory to store images to be preprocessed
    imageQueue=[]
    def __init__(self):
        self.fetchImages(imageDir)

    def fetchImages(self,image_directory):
        # glob function finds files with the given pattern here is the string in image_directory
        self.m_imagelist = glob(image_directory+"*")
        for imageName in self.m_imagelist:
            m_image = Image.open(imageName)
            ImageConverter.imageQueue.append(m_image)
            # print(self.image.size,self.image.mode)
    
    def resizeImage(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageQueue[:]
        ImageConverter.imageQueue[:] = []
        for image in m_temporaryImageList:
            # here (500,500) is the image width and height
            resizedImage = image.resize((500,500),Image.ANTIALIAS)
            ImageConverter.imageQueue.append(resizedImage)
        m_temporaryImageList[:] = []

    def convertToGrayScale(self):
        m_temporaryImageList = []
        m_temporaryImageList[:] = ImageConverter.imageQueue[:]
        ImageConverter.imageQueue[:] = []
        for image in m_temporaryImageList:
            blackWhiteImage = image.convert('L')
            ImageConverter.imageQueue.append(blackWhiteImage)
        del m_temporaryImageList

    @staticmethod
    def showImageQueue():
        print(ImageConverter.imageQueue)

    @staticmethod
    def saveImages():
        for index,imageObject in enumerate(ImageConverter.imageQueue):
            # image quality is being reduced to 95% with quality flag
            imageObject.save(imageDir+str(index+1)+"_new.jpg",quality = 95)
        


imageConverter = ImageConverter()
imageConverter.convertToGrayScale()
# ImageConverter.showImageQueue()
ImageConverter.saveImages()