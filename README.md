# Knuckle print recognition

*Dependencies*
* argparse
* scipy
* numpy
* matplotlib
* pandas
* skimage
* opencv

**HOW TO EXECUTE**
1. First create a file named setup.config and paste the image directory
    <pre>imageRootPath = C:\pathtothedirectory </pre>
		
2. run:
<pre>python app.py --convert_to_grayscale --normalize_images --segment_images --create_vector</pre>
 <br>
 This will create a 1D matrix which will be saved in a file named in dataset.csv
 
3. edit

**Directory structure**
<pre>

C:\knuckle-print-recognition
|   .gitignore
|   createdataset.py
|   find_image.py
|   parse_config.py
|   README.md
|   setup.config
|   trainmodel.py
|   dataset.csv 
\---Preprocessing
        imageconverter.py
        

</pre>

## Intuition:

### Image Dataset Preprocessing
Preprocessing steps-
- [x] 1. Conversion of RGB knuckle prints to Grayscale patterns: The first step of preprocessing is that the RGB knuckle prints are converted into gray scale images.
- [x] 2. Addition of Noise: Although we will try to keep the pictures of the image as noiseless as possible, but it is really essential to check whether our algorithm will be able to tackle images of knuckle prints with noises. To check the same as mentioned, we add noise to the images.
- [x] 3. Blur: To check that our algorithm also is able to tackle a Blurred Image upto a certain extent, we Blur the picture of the  knuckle print images and thus proceed further.
- [x] 4. Removal of Noise: Noise is certain to arise in the pictures, and thus if the pictures of the  knuckle prints images are noisy, then noises are removed from  knuckle prints images to help in better recognition of the image. In this process 2D Median Filter have been used.
- [x] 5. Deblurring: Next step is to Deblur the parts of the image. We use Wiener Filter have been used to De Blur the blurred images to Deblur the Blurred parts so that the edges and the sharpness of the points in the images do not get destroyed and the knuckle print image is recognizable easily for processing.
- [x] 6. Image Normalisation: The normalization is a process that changes the range of pixel intensity values. Basically it has two steps. The first one is to "cut" values too high or too low. i.e. if the image matrix has negative values one set them to zero and if the image matrix has values higher than max value one set them to max values. The second one is to linear stretch all the values in order to fit them into the interval [0, max value].
- [x] 7. Conversion of Gray scale images into Binary Images: This process converts the gray scale patterns into binary image (2D matrix file). We Convert a Grayscale Image to Binary Image using Thresholding. Thresholding is the simplest method of image segmentation and the most common way to convert a grayscale image to a binary image.
- [x] 8. Conversion of compressed Binary Patterns into 1D vector: Finally the 2D matrix knuckle print files are converted into its corresponding 1D vector files.
This set then become the input of the OCA.
