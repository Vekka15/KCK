#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math
from matplotlib import colors
import csv

def load_data():
    #matrix = [[0 for x in range(500)] for x in range(501)]
    matrix = np.zeros((500,500))
    i=0
    j=0
    with open('big.dem', 'r') as f:
        reader = csv.reader(f)
        for column in reader:
            ble=0
            column=column[0].split(' ')
            del column[-1]
            for ele in column:
                if(float(ele)==500.0):
                    print('weszlo')
                    ble=1
                    break
                else:
                    matrix[i][j]=ele
                    j=j+1
            if ble!=1:
                i=i+1
                j=0
    return matrix

def map_gradient(v):
    if v<=0.5:
        red=2*v
        green=1
        blue=0
    else:
        red=1
        green=2-2*v
        blue=0
    return red,green,blue

def draw_plot(macierz):
    ax=plt.plot()
    img = np.zeros((500, 500, 3))
    mini=np.amin(macierz)
    maxi=np.amax(macierz)
    for i in np.arange(500):
        for j in np.arange(500):
            v=(macierz[i][j]-mini)/(maxi-mini)
            img[i,j]=map_gradient(v)
    plt.imshow(img)
    plt.savefig('map.pdf')

if __name__ == '__main__':
    macierz=load_data()
    draw_plot(macierz)
