import Image
import sys

image=Image.open('spinalcord.jpg')
image.load()

imageSize = image.size
imageBox = image.getbbox()

imageComponents = image.split()

rgbImage = Image.new("RGB", imageSize, (0,0,0))
rgbImage.paste(image, mask=imageComponents[3])
croppedBox = rgbImage.getbbox()
print imageBox
print croppedBox
if imageBox != croppedBox:
    cropped=image.crop(croppedBox)
    print 'spinalcord.jpg:', "Size:", imageSize, "New Size:",croppedBox
    cropped.save('spinalcord_cropped.jpg')
