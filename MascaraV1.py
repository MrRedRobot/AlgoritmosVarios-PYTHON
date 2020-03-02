# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:24:18 2018

@author: DAv_O
"""

import numpy as np
import PIL as pil

I = np.asarray(pil.Image.open('Skull.jpg'))

img = pil.Image.open("Skull.jpg").convert("L")
imgarr = np.array(img)


