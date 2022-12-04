# fix this shiz
import os
import math
import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance
from colorthief import ColorThief
from colour import Color
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# image dimensions
box = (int((980/2)), int((980/2)))
full = (1280, 720)
W, H = (int((1000/2)), int((1000/2)))

font = ImageFont.truetype('/Library/Fonts/Herculanum.ttf', int(200/2))

def thumbnail(img):
    image = Image.open(img).convert("RGBA")

    # add filter
    filter = ImageEnhance.Contrast(image)
    filter.enhance(.75).save('content/fade.png')
    fade = Image.open('content/fade.png')
    print('filter added')

    # add backdrop
    edit = ImageOps.fit(fade, box, Image.ANTIALIAS)
    edit.save('content/edit.png')

    # add border
    backdrop = Image.new('RGB', (W, H), (0, 0, 0))
    backdrop_edit = ImageOps.fit(backdrop, (W, H), Image.ANTIALIAS)
    backdrop_edit.paste(edit, (5, 5), mask = edit)
    # # add title 
    # sq = ImageDraw.Draw(backdrop_edit)
    # str = wav.split('"')
    # title = str[1]
    # w, h = sq.textsize(title, font=font)
    # sq.text(((W-w)/2,(H-h)/2), title, font=font, fill="white")
    backdrop_edit.save('content/sq.png')

    # create background gradient
    # gradient()

    # create background color
    background()

    # pastes sq onto gradient img
    full_backdrop = Image.open('content/full.png')
    full_backdrop_edit = ImageOps.fit(full_backdrop, full, Image.ANTIALIAS)
    full_backdrop_edit.paste(backdrop_edit, (390, 110))
    full_backdrop_edit.save('content/thumb.png')

    # delete extra png files
    filelist = [ f for f in os.listdir('content') if f.endswith(".png") ]
    for f in filelist:
        if f.endswith('thumb.png') or f.endswith('sq.png'):
            pass
        else:
            os.remove(os.path.join('content', f))
    print('thumbnail created')

def gradient():
    ct = ColorThief('content/edit.png')
    palette = ct.get_palette(color_count=2, quality=1)
    w = 1280
    c1 = palette[0]
    c2 = palette[1]
    i = (c1[0] - c2[0]) / w
    j = (c1[1] - c2[1]) / w
    k = (c1[2] - c2[2]) / w
    img = Image.new('RGBA', full)
    for y in range(1280):
        for x in range(720):
            img.putpixel((y, x), (math.ceil((c1[0] - i * y)), math.ceil((c1[1] - j * y)), math.ceil((c1[2] - k * y))))
    img.save('content/full.png')
    print('gradient created from dominant colors')

def background():
    ct = ColorThief('content/edit.png')
    color = ct.get_color(quality=1)
    img = Image.new('RGB', full, color)
    img.save('content/full.png')
    print('background created from dominant color')


