Title: Narrative Clip Script to make mp4 from images
Date: 2016-06-02
Tags: narrativeclip,gadget,script,python


```
import glob
import PIL.Image as Image
import sys
import os
import re

param = sys.argv

try:
    pattern = r"\d{4}/\d{2}/\d{2}"
    flag = re.match(pattern, param[1])
    if not flag:
        raise Exception
except:
    print("arg is yyyy/MM/dd")
    sys.exit(1)

files = glob.glob('{0}/*.jpg'.format(param[1]))

convert_image = {
    1: lambda img: img,
    2: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),
    3: lambda img: img.transpose(Image.ROTATE_180),
    4: lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),
    5: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90),
    6: lambda img: img.transpose(Image.ROTATE_270),
    7: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270),
    8: lambda img: img.transpose(Image.ROTATE_90),
}

for i, file in enumerate(files):
    print(file)
    img = Image.open(file)
    exif = img._getexif()
    orientation = exif.get(0x112, 1)
    new_img = convert_image[orientation](img)
    w = new_img.size[0]
    h = new_img.size[1]
    if w > h:
        l = h
        diff = (w - h) / 2
        s = new_img.crop((diff, 0, w - diff, h))
    else:
        l = w
        diff = (h - w) / 2
        s = new_img.crop((0, diff, w, h - diff))

    counter = 0
    pix = s.resize((100, 100)).load()
    for j in range(100):
        for k in range(100):
            if pix[j, k][0] < 20 and pix[j, k][1] < 20 and pix[j, k][2] < 20: counter += 1
    if counter < 5000: s.save('{0}/source{1:05d}.jpg'.format(param[1], i), "JPEG")

os.system('ffmpeg -f image2 -r 2 -i {0}/source%05d.jpg -r 2 -an -vcodec libx264 -pix_fmt yuv420p {0}/video.mp4'.format(param[1]))
os.system('rm {0}/source%05d.jpg'.format(param[1]))
```

put this script on `clip_?????` dir
and execute this script like `python script.py yyyy/MM/dd`  
then video.mp4 will be made in `clip_?????/yyyy/MM/dd/video.mp4`
