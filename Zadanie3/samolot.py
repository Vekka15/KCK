#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from pylab import *
# import skimage
# from skimage import data, io, exposure, filters
# from skimage import feature
# from skimage.filter.edges import convolve
# from skimage import img_as_float, img_as_ubyte
import scipy
from pylab import *
import skimage
from skimage import data, io, filters, exposure, feature
from skimage.filters import rank
from skimage.util.dtype import convert
from skimage import img_as_float, img_as_ubyte
from skimage.io import Image
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
from skimage.filters.edges import convolve
from skimage.filters import threshold_otsu, threshold_adaptive
from matplotlib import pylab as plt
import numpy as np
from numpy import array
import Image
from skimage import data, io, morphology
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
from pylab import *
#from skimage.io import Image
from skimage.morphology import square
import skimage as si
import numpy as np
from numpy import array
import matplotlib.pyplot as pl

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

# #canny + sobel
if __name__ == '__main__':
    picture_table=['samolot17.jpg','samolot05.jpg','samolot10.jpg','samolot11.jpg','samolot12.jpg','samolot01.jpg']
    wyn_table = ['wynik.jpg','wynik1.jpg','wynik2.jpg','wynik3.jpg','wynik4.jpg','wynik5.jpg']
    new_im = Image.new('RGB', (600,600))
    i=0
    j=0
    for index,image in enumerate(picture_table):
        im = Image.open(image)

        img = img_as_float(data.imread(image))
        tmp = rgb2gray(img)
        global_thresh = threshold_otsu(tmp)
        binary_global = tmp > global_thresh
        # block_size = 5
        # binary_adaptive = threshold_adaptive(tmp, block_size, offset=10)
        sob = filters.sobel(binary_global)**0.9
        #final= skimage.feature.canny(sob, sigma=1)

        #
        # img = skimage.feature.canny(tmp, sigma=1)
        scipy.misc.imsave(wyn_table[index],sob)
        picture = Image.open(wyn_table[index])
        picture.thumbnail((300,200))
        new_im.paste(picture, (i, j))
        if(index==2):
            print(index)
            i=i+300
            j=0
        else:
            print(index)
            j=j+200

    new_im.save('merge.png')
    #plt.savefig('map.pdf')
