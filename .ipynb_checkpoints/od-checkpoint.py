#import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import time
import os
from PIL import Image

print('he;')

image = Image.open("/Users/allester/Documents/dining_cams/data/bee1.png")
image.thumbnail((64,64))
imgplot = plt.imshow(image)
imgplot