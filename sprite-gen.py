import os
from PIL import Image
import glob
iconMap =  sorted(glob.glob('C:\Users\Valentin\Documents\magshimim\imgset\*'))
images = [Image.open(filename) for filename in iconMap][:120]
#images = [Image.open(filename) for filename in iconMap][::2]

image_width, image_height = images[0].size


images_count = len(images)
cols_count = 10 #pics per row
rows_count = int(images_count/cols_count) + bool(images_count%cols_count)
totalsize = cols_count*image_width , rows_count*image_height

#print cols_count,rows_count,totalsize

master = Image.new(
    mode='RGB',
    size=totalsize,
    color=(255,255,255))





for y in range(rows_count):
    for x in range(cols_count):
        location = x*image_width,y*image_height
        num = cols_count*y + x
        if num >= len(images):
            images.insert(num, Image.new(    mode='RGB',    size=(image_width, image_height),    color=(255,255,255)))        
        image = images[num]
        #out = image.resize((image_width, image_height))
        master.paste(image,location)
        print "col %s,row %s, loc %sx%s, num %s, %s" % (x,y,location[0],location[1], num,image  )


 


master.save('C:\Users\Valentin\Documents\magshimim\output\s800q50.jpg', format="JPEG" , quality=50)
smallsize = 5000,6000
small = master.resize(smallsize, Image.ANTIALIAS)
small.save('C:\Users\Valentin\Documents\magshimim\output\s500q75.jpg', format="JPEG" , quality=75)

