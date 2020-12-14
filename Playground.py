import os
from PIL import Image


def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    out = img.resize((width, height),Image.ANTIALIAS)  # resize image with high-quality
    out.save(fileout, type)


if __name__ == '__main__':
    '''
    修改所有贴图至30x30大小
    '''

    for file in os.listdir('Sprites'):
        fileIn = "Sprites/" + file
        fileOut = "pics_test/" + file
        fileType = 'png'
        WIDTH = 30
        HEIGHT = 30
        ResizeImage(fileIn, fileOut, WIDTH, HEIGHT, fileType)