import glob
import PIL.Image as Image
import sys
import os
import re
import cv2

param = sys.argv

try:
    pattern = r"\d{4}/\d{2}/\d{2}"
    flag = re.match(pattern, param[1])
    if len(param) < 3 or not flag or not int(param[2]):
        raise Exception

except:
    print("arg is {yyyy/MM/dd} {fps}")
    sys.exit(1)

# rotate images by its exif, and crop them to square
files = glob.glob('{0}/[0-9]*.jpg'.format(param[1]))
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
    try:
        print(file)
        img = Image.open(file)
        exif = img._getexif()
        if exif is not None:
            orientation = exif.get(0x112, 1)
            img = convert_image[orientation](img)

        w = img.size[0]
        h = img.size[1]

        if w > h:
            l = h
            diff = (w - h) / 2
            s = img.crop((diff, 0, w - diff, h))
        else:
            l = w
            diff = (h - w) / 2
            s = img.crop((0, diff, w, h - diff))
        counter = 0
        pix = s.resize((50, 50)).load()
        for j in range(50):
            for k in range(50):
                if pix[j, k][0] < 40 and pix[j, k][1] < 40 and pix[j, k][2] < 40: counter += 1
        # remove black images
        if counter < 2000: s.save('{0}/source{1:05d}.jpg'.format(param[1], i), "JPEG")
    except Exception as e:
        print("can not open " + file)
        print(str(type(e)))

# pixelate each images if it has face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
files = glob.glob('{0}/source*.jpg'.format(param[1]))

for file in files:
    print(file + " mosaic")
    img = cv2.imread(file)
    result = cv2.imread(file)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    face = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=1, minSize=(30, 30))

    if 0 < len(face):

        for (x, y, w, h) in face:
            cut_img = img[y:y + h, x:x + w]
            cut_face = cut_img.shape[:2][::-1]
            # the size of being pixelated
            cut_img = cv2.resize(cut_img, (int(cut_face[0] / 15), int(cut_face[0] / 15)))
            cut_img = cv2.resize(cut_img, cut_face, interpolation=cv2.INTER_NEAREST)
            result[y:y + h, x:x + w] = cut_img

    cv2.imwrite(file, result)
    cv2.destroyAllWindows()

os.system('ffmpeg -f image2 -r {1} -i {0}/source%05d.jpg -r {1} -an -vcodec libx264 -pix_fmt yuv420p {0}/video.mp4'.format(param[1],param[2]))



