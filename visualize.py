from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tifffile as tif
import os

if not os.path.isdir("results"):
    os.mkdir("results")

for name in os.listdir("/home/DataSet/Omnipose_test_rgb/masks/"):
    image = tif.imread("/home/DataSet/Omnipose_test_rgb/masks/"+name)
    plt.imsave("/home/cvml_omnipose/results/"+name+".png",image)