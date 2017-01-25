from PIL import Image
import sys
import glob

names = glob.glob('*g')
names = [n for n in names if '_cropped' not in n]

#image.load()
#names = ['neurovault.jpg', 'modelgui.png']
for name in names:
    image=Image.open(name)
    imageSize = image.size
    print name
    if imageSize[1] > 250:
        image=image.resize( (374,250), Image.ANTIALIAS)
        parts = name.split('.')
        image.save(parts[0]+'_cropped.'+parts[1])
        print name
#imageBox = image.getbbox()
#cropped=image.crop(imageBox)

#cropped.save('spinalcord_cropped.jpg')
