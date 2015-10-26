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

def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True)
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v) #wywołujemy sobie każdą funkcje z v

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def gradient_rgb_bw(v):
    #TODO
    return (v, v, v)


def gradient_rgb_gbr(v): # red green blue
    # if v<=0.5:
    #     red=0
    #     green=1-2*v
    #     blue=2*v
    # else:
    #     red=2*v-1
    #     green=0
    #     blue=2-2*v
    if v<=0.5:
        red=2*v
        green=1
        blue=0
    else:
        red=1
        green=2-2*v
        blue=0
    return (red, green, blue)


def gradient_rgb_gbr_full(v):
    if v<=0.25:
        red=0
        green=1
        blue=4*v
    if v<=0.5 and v>0.25:
        red=0
        blue=1
        green=2-4*v
    if v<=0.75 and v>0.5:
        green=0
        blue=1
        red=4*v-2
    if v>0.75:
        red=1
        green=0
        blue=4-4*v

    return (red, green, blue)


def gradient_rgb_wb_custom(v):
    if v<= (1.0/7.0): # bialy na magenta
        red=1
        blue=1
        green=1-7*v
    if v> (1.0/7.0) and v<= (2.0/7.0): # magenta na niebieski
        red=2-7*v
        green=0
        blue=1
    if v>(2.0/7.0) and v<= (3.0/7.0): # niebieski na cyan
        red=0
        green=7*v-3
        blue=1
    if v>(3.0/7.0) and v<=(4.0/7.0): # cyan na zielony
        red=0
        green=1
        blue=4-7*v
    if v>(4.0/7.0) and v<=(5.0/7.0): # zielony na zółty
        red=7*v-5
        green=1
        blue=0
    if v>(5.0/7.0) and v<=(6.0/7.0): #żółty na czerwony
        red=1
        green=6-7*v
        blue=0
    if v>(6.0/7.0):
        red=7-7*v
        green=0
        blue=0
    return (red, green, blue)


def gradient_hsv_bw(v): #bo kolor jest dowolny jasnosc jest 0 i wartosc wzrastamy od czarnego do bialego
    r=(1-v-0.2)*360
    print(r)
    b=1-v
    return hsv2rgb(r, 0, b)


def gradient_hsv_gbr(v): #dokonczyc
    if v<0.2:
        r=((0.8+v)*360)
        b=1-v
    else:
        r=(v-0.2)*0.6*360
        b=1-v
    return hsv2rgb(r, 0.996, 1)

def gradient_hsv_unknown(v):
    r=v*360
    return hsv2rgb(r, 0.5, 0.5)


def gradient_hsv_custom(v):
    #TODO
    return hsv2rgb(0, 0, 0)


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
