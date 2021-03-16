import PIL
print('Pillow Version:', PIL.__version__)

from PIL import Image
# Open the image form working directory
image = Image.open('download.jpg')
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
load_image.show()

from matplotlib import image
from matplotlib import pyplot
# load image as pixel array
image = image.imread('download.jpg')
# summarize shape of the pixel array
print(image.dtype)
print(image.shape)
# display the array of pixels as an image
pyplot.imshow(image)
pyplot.show()

from PIL import Image
from numpy import asarray
# load the image
image = Image.open('download.jpg')
# convert image to numpy array
data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)

print(data)