# Knuckle print recognition

## Preprocessing
Preprocessing steps-
1. Conversion of RGB knuckle prints to Grayscale patterns: The first step of preprocessing is that the RGB knuckle prints are converted into gray scale images. Conversion of a color image into a grayscale image inclusive of salient features is a complicated process. The converted grayscale image may lose contrasts, sharpness, shadow, and structure of the color image. To preserve contrasts, sharpness, shadow, and structure of the color image a new algorithm has proposed. To convert the color image into grayscale image the new algorithm performs RGB approximation, reduction, and addition of chrominance and luminance. The grayscale images generated using the algorithm in the experiment confirms that the algorithm has preserved the salient features of the color image such as contrasts, sharpness, shadow, and image structure.
2. Addition of Noise: Although we will try to keep the pictures of the image as noiseless as possible, but it is really essential to check whether our algorithm will be able to tackle images of knuckle prints with noises. To check the same as mentioned, we add noise to the images.
3. Blur: To check that our algorithm also is able to tackle a Blurred Image upto a certain extent, we Blur the picture of the  knuckle print images and thus proceed further.
4. Removal of Noise: Noise is certain to arise in the pictures, and thus if the pictures of the  knuckle prints images are noisy, then noises are removed from  knuckle prints images to help in better recognition of the image. In this process 2D Median Filter have been used.
5. Deblurring: Next step is to Deblur the parts of the image. We use Wiener Filter have been used to De Blur the blurred images to Deblur the Blurred parts so that the edges and the sharpness of the points in the images do not get destroyed and the knuckle print image is recognizable easily for processing.
6. Image Normalisation: The normalization is a process that changes the range of pixel intensity values. Basically it has two steps. The first one is to "cut" values too high or too low. i.e. if the image matrix has negative values one set them to zero and if the image matrix has values higher than max value one set them to max values. The second one is to linear stretch all the values in order to fit them into the interval [0, max value].
7. Conversion of Gray scale images into Binary Images: This process converts the gray scale patterns into binary image (2D matrix file). We Convert a Grayscale Image to Binary Image using Thresholding. Thresholding is the simplest method of image segmentation and the most common way to convert a grayscale image to a binary image.
8. Image Compression: In this step, the images are compressed by replacing blocks of pixels with the mode value of the pixel intensities where mode is the intensity value which has occurred more frequently in the block.
The steps to compress a knuckle print image are as follows: 
	* Count the number of pixels of knuckle print image.
	* Find the block size such that compressed image is of size 128×96 pixels.
	* Find the mode of the pixel intensities in each block.
	* Replace each block by its corresponding mode intensity to obtain equivalent compressed image of size 128×96 pixels.

9. Conversion of compressed Binary Patterns into 1D vector: Finally the 2D matrix knuckle print files are converted into its corresponding 1D vector files.
This set then become the input of the OCA.