AUTHOR = "BIKRAM MODAK"
print("***************** WELCOME TO KNUCKLE PRINT RECOGNITION SYSTEM *****************")
import argparse
from Preprocessing.imageconverter import ImageConverter


# other setup variables will be added later
with open("setup.config",'r') as setupfile:
    imageDir = setupfile.read()

print("\n\nLoading... ",end='')
print(imageDir)

parser = argparse.ArgumentParser()
parser.add_argument("--convert_to_grayscale", help="convert images to grayscale", action="store_true")
parser.add_argument("--add_noise", help="add noise to the images", action="store_true")
parser.add_argument("--add_blur", help="add noise to the images", action="store_true")
parser.add_argument("--de_noise", help="de noising/smoothing of images", action="store_true")
parser.add_argument("--restore_images", help="restore images", action="store_true")
parser.add_argument("--normalize_images", help="normalize images", action="store_true")
parser.add_argument("--show_images", help="show images in different window", action="store_true")
parser.add_argument("--save_images", help="save images in a different folder", action="store_true")

args = parser.parse_args()

imageConverter = ImageConverter(imageDir)
# imageConverter.getOriginalImages()
if args.convert_to_grayscale:
    imageConverter.convertToGrayScale()
    # ImageConverter.showImageQueue()
if args.add_noise:
    imageConverter.add_noise()
    # imageConverter.getBlurValue()
    # ImageConverter.showImage("After adding noise getting blur value")
    # ImageConverter.showImageQueue()
if args.add_blur:
    imageConverter.addBlur()
    # imageConverter.getBlurValue()
    # ImageConverter.showImage("After adding blur getting blur value")
if args.de_noise:
    imageConverter.de_noise()
    # imageConverter.getBlurValue()
    # ImageConverter.showImage("After denoising getting blur value")
    # ImageConverter.showImageQueue()
if args.restore_images:
    imageConverter.deblurring()
    # imageConverter.getBlurValue()
    # ImageConverter.showImage("After removing blur getting blur value")
if args.normalize_images:
    imageConverter.normalizeImages()
    # ImageConverter.showImage("After normalizing")
    # ImageConverter.showImageQueue()
if args.show_images:
    ImageConverter.showImage("Image")
if args.save_images:
    ImageConverter.saveImage()