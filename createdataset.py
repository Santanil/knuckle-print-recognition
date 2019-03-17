AUTHOR = "BIKRAM MODAK"
print("***** WELCOME TO KNUCKLE PRINT RECOGNITION SYSTEM *****")
import argparse
from Preprocessing.imageconverter import ImageConverter
from parse_config import ParseConfig
from find_image import ImageFetch
from apputility import printProgressBar
import os

####################
# Global Variables #
####################
imageRootPath = ""
fifo_process_images_of_every_person_objects = []

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
parser.add_argument("--debug",help ="Used to debug",action = "store_true")
parser.add_argument("--createcsvfile",help = "Writes data in matrix into a file",action = "store_true")
args = parser.parse_args()

configparser = ParseConfig()

if 'imageRootPath' in configparser.configs.keys():
    imageRootPath = configparser.configs['imageRootPath']

imageFetch = ImageFetch(imageRootPath)

no_of_individuals = imageFetch.totalnumberofindividuals()

list_of_per_person_finger_wise_folders = imageFetch.getimageperpersonimagelist()

if args.debug:
    print(no_of_individuals)
    print(imageRootPath)
    for personfolderpath in list_of_per_person_finger_wise_folders:
        for folderpath in personfolderpath:
            print(folderpath)

def processImages():
    global no_of_individuals
    try:
        # Initial call to print 0% progress
        printProgressBar(0, no_of_individuals, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i in range(0, no_of_individuals):
            fifo_process_images_of_every_person_objects.append(
                ImageConverter(list_of_per_person_finger_wise_folders[i]))
            if args.convert_to_grayscale:
                fifo_process_images_of_every_person_objects[i].convertToGrayScale()
            if args.de_noise:
                fifo_process_images_of_every_person_objects[i].de_noise()
            # if args.normalize_images:
            #     fifo_process_images_of_every_person_objects[i].normalizeImages()
            if args.create_vector:
                fifo_process_images_of_every_person_objects[i].imageToVector()
            printProgressBar(i + 1, no_of_individuals, prefix = 'Progress:', suffix = 'Complete', length = 50)
    except:
        print("error " + str(TypeError))

processImages()


print("Preprocessing Done.")

if args.createcsvfile:
    ImageConverter.writetodatasetfile()
if args.debug:
    ImageConverter.showimageFIFO()

if args.show_images:
    ImageConverter.showImage("Image")

print("Exiting...")
if (os.path.isfile("cleanup.bat")):
    os.system("cleanup.bat")
