from PIL import Image
import sys

image=Image.open('spinalcord.jpg').resize( (200,200), Image.ANTIALIAS)
#image.load()

#imageSize = image.size
#imageBox = image.getbbox()
#cropped=image.crop(imageBox)
image.save('spinalcord_cropped.jpg')
#cropped.save('spinalcord_cropped.jpg')
