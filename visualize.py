from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tifffile as tif
import os

dir_path = "/home/DataSet/Omnipose_val/masks/"

if not os.path.isdir("results"):
    os.mkdir("results")

for name in os.listdir(dir_path):
    image = tif.imread(dir_path+name)
    plt.imsave("/home/cvml_omnipose/results/"+name+".png",image)