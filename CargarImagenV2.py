# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 21:23:23 2018

@author: DAv_O
"""

from PIL import Image
import numpy as np

im = Image.open('Skull.jpg')
#im = Image.open('Skull.jpg')
im = im.convert('L')

arr = np.fromiter(iter(im.getdata()), np.uint8)
arr.resize(im.height, im.width)

arr ^= 0xFF  # invert
inverted_im = Image.fromarray(arr, mode='L')
inverted_im.show()

pix = im.load()

print(pix)
