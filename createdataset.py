AUTHOR = "BIKRAM MODAK"
print("***** WELCOME TO KNUCKLE PRINT RECOGNITION SYSTEM *****")
print("///// BIKRAM MODAK /////")
import argparse
from Preprocessing.imageconverter import ImageConverter
from parse_config import ParseConfig
from find_image import ImageFetch
from pprint import pprint
from functools import lru_cache

####################
# Global Variables #
####################
imageRootPath = ""
# preprocessed_dataset = np.empty()

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

configparser = ParseConfig()
if 'imageRootPath' in configparser.configs.keys():
    imageRootPath = configparser.configs['imageRootPath']

imageFetch = ImageFetch(imageRootPath)

no_of_individuals = imageFetch.totalnumberofindividuals()

list_of_per_person_finger_wise_folders = imageFetch.getimageperpersonimagelist()

fifo_process_images_of_every_person_objects = []

pprint("Processing 591 images")

@lru_cache(maxsize=4000)
def processImages():
    global no_of_individuals
    try:
        for i in range(0, no_of_individuals + 1):
            print("Processing image of individual:", i + 1)
            fifo_process_images_of_every_person_objects.append(
                ImageConverter(list_of_per_person_finger_wise_folders[i]))
            if args.convert_to_grayscale:
                fifo_process_images_of_every_person_objects[i].convertToGrayScale()
            if args.normalize_images:
                fifo_process_images_of_every_person_objects[i].normalizeImages()
            if args.segment_images:
                fifo_process_images_of_every_person_objects[i].imageSegmentation()
            if args.create_vector:
                fifo_process_images_of_every_person_objects[i].imageToVector()
    except:
        print("error " + str(TypeError))

processImages()


pprint("Preprocessing Done.")

# ImageConverter.writetodatasetfile()

ImageConverter.showimageFIFO()

if args.show_images:
    ImageConverter.showImage("Image")

pprint("Exiting...")
