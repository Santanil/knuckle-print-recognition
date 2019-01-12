AUTHOR = "BIKRAM MODAK"
print("***** WELCOME TO KNUCKLE PRINT RECOGNITION SYSTEM *****")
print("///// BIKRAM MODAK /////")
import argparse
from Preprocessing.imageconverter import ImageConverter


# configuration file for settings
# other setup variables will be added later
with open("setup.config",'r') as setupfile:
    imageDir = setupfile.read()

print("\n\nLoading... ",end='')
print(imageDir,"\n")

# command line options and flags
parser = argparse.ArgumentParser()
parser.add_argument("--convert_to_grayscale", help="convert images to grayscale", action="store_true")
parser.add_argument("--add_noise", help="add noise to the images", action="store_true")
parser.add_argument("--add_blur", help="add noise to the images", action="store_true")
parser.add_argument("--de_noise", help="de noising/smoothing of images", action="store_true")
parser.add_argument("--restore_images", help="restore images", action="store_true")
parser.add_argument("--normalize_images", help="normalize images", action="store_true")
parser.add_argument("--show_images", help="show images in different window", action="store_true")
parser.add_argument("--save_images", help="save images in a different folder", action="store_true")
parser.add_argument("--segment_images",help = "transforms images into binary format",action = "store_true")
parser.add_argument("--create_vector",help = "transforms image data into 1D array aka vector",action = "store_true")
parser.add_argument("--compress_images",help = "compresses images",action = "store_true")

args = parser.parse_args()

# image preproccessing 
# image converter initialization
imageConverter = ImageConverter(imageDir)

# converting images to desired form
if args.convert_to_grayscale:
    imageConverter.convertToGrayScale()
if args.add_noise:
    imageConverter.add_noise()
if args.add_blur:
    imageConverter.addBlur()
if args.de_noise:
    imageConverter.de_noise()
if args.restore_images:
    imageConverter.deblurring()
if args.normalize_images:
    imageConverter.normalizeImages()
if args.compress_images:
    imageConverter.compressImages()
if args.segment_images:
    imageConverter.imageSegmentation()
if args.create_vector:
    imageConverter.imageToVector()
if args.show_images:
    ImageConverter.showImage("Image")
if args.save_images:
    ImageConverter.saveImage()